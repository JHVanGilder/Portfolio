from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

"""
loads and centers all images at the mean of each axis
input: str: filename: name of the file of the image
output: np.array: centered image array
"""
def load_and_center_dataset(filename):
    x = np.array(np.load(filename))
    x = x - np.mean(x, axis = 0)
    return x

"""
generates covariance of the input array
input: np.array: dataset: image array
output: np.array: image covariance matrix
"""
def get_covariance(dataset):
    return np.cov(dataset, rowvar = False)

"""
generates m largest eigenvalue and eigenvector arrays
input: np.array: S: image to get eigenvalues from
        int: m: number of eigenvalues to be returned
output: greatest m eigenvalues and corresponding 
        eigenvectors
"""
def get_eig(S, m):
    max_list = []
    max_i_list = []
    values, vectors = eigh(S)
    max_vector_list = []
    a = np.zeros((m,m))
    for j in range(m):
        max = 0
        max_i = 0
        for i in range(len(values)):
            if (values[i] > max) and (values[i] not in max_list):
                max = values[i]
                max_i = i
        max_list.append(max)
        max_i_list.append(max_i)
    for y in range(m):
        a[y][y] = max_list[y]
    for w in range(m):
        a[w][w] = max_list[w]
    for q in range(len(values)):
        vector = []
        for u in range(2):
            vector.append(vectors[:, max_i_list[u]][q])
        max_vector_list.append(vector)

    return a, max_vector_list

"""
generates eigenvalue and eigenvector arrays of values
    within prop of the sva
input: np.array: S: image to get eigenvalues from
        int: m: number of eigenvalues to be returned
output: prop sva eigenvalues and corresponding 
        eigenvectors
"""
def get_eig_prop(S, prop):
    values, vectors = eigh(S)
    eig_sum = 0
    over_list = []
    over_loc = []
    over_vectors = []
    for value in values:
        eig_sum += value
    for w in range(len(values)):
        eig_val = values[w]
        if eig_val/eig_sum > prop:
            over_list.append(eig_val)
            over_loc.append(w)
    over_list.sort()
    over_list.reverse()
    a = np.zeros((len(over_list), len(over_list)))
    m = len(over_list)
    for i in range(len(over_list)):
        a[i][i] = over_list[i]
    for q in range(len(values)):
        vector = []
        for u in range(2):
            vector.append(vectors[:, over_loc[u]][q])
        vector.reverse()
        over_vectors.append(vector)
    return a, over_vectors

"""
generates projections of input image
input: image: image to be projected
       array: U: cov matrix of image
output: list: proj_x: projected image
"""
def project_image(image, U):
    x = image
    m = len(U)
    proj_x = []
    for i in range(m):
        u = U[i]
        u_t = np.transpose(U)
        u_t * x
        proj_x.append(np.dot(np.dot(u_t, x), u))
    return proj_x

"""
displays image and projected image
input: array: orig: original image data array
       array: projected image data array
output: none
"""

def display_image(orig, proj):
    orig_2d = np.reshape(orig, (32, 32))
    proj_2d = np.reshape(proj, (32, 32))
    orig_2d_t = np.transpose(orig_2d)
    proj_2d_t = np.transpose(proj_2d)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title("Original")
    ax2.set_title("Projection")
    im1 = ax1.imshow(orig_2d_t, aspect='equal')
    im2 = ax2.imshow(proj_2d_t, aspect='equal')
    fig.colorbar(im1, ax=ax1, shrink=.5)
    fig.colorbar(im2, ax=ax2, shrink=.5)
    plt.show()
    pass

x = load_and_center_dataset('YaleB_32x32.npy')
S = get_covariance(x)
Lambda, U = get_eig(S, 2)
projection = project_image(x[0], U)
display_image(x[0], projection)