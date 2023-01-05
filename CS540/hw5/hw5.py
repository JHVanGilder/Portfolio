import csv
import matplotlib.pyplot as plt
import numpy as np

def visualize_data(filename):
    x = []
    y = []
    with open(filename) as csv_file:
        reader = list(csv.reader(csv_file))
        for row in reader[1:]:
            x.append(int(row[0]))
            y.append(int(row[1]))
    plt.plot(x, y)
    plt.ylabel("Number of frozen days")
    plt.xlabel("Year")
    plt.xticks(np.arange(min(x), max(x)+1, 20))
    plt.savefig("plot.jpg")

def linear_regression(filepath):
    with open(filepath) as csv_file:
        reader = list(csv.reader(csv_file))
        n = len(reader) -1
        X = np.ones((n, 2))
        Y = []

        for i in range(len(reader[1:])):
            X[i][1] = int(reader[i+1][0])
            Y.append(int(reader[i+1][1]))
    X_T = np.transpose(X)
    Z = np.matmul(X_T, X)
    I = np.linalg.inv(Z)
    PI = np.matmul(I, X_T)
    B = np.matmul(PI, Y)
    print("Q3a:")
    print(X)
    print("Q3b:")
    print(Y)
    print("Q3c:")
    print(Z)
    print("Q3d:")
    print(I)
    print("Q3e:")
    print(PI)
    print("Q3f:")
    print(B)

    y_test = B[0] + B[1]*2021
    print("Q4: " + str(y_test))
    if (B[1] > 0):
        print("Q5a: >")
    elif (B[1] == 0):
        print("Q5a: =")
    elif (B[1] < 0):
        print("Q5a: <")
    print("Q5b: This means that the general trend of the data is downward")
    x_0 = abs(B[0]/B[1])
    print("Q6a:")
    print(x_0)
    print("Q6b: It isn't a good model because there are advancements and "
          "changes in society that would make a linear regression not a "
          "good data model in this situation. Also, there is no reason "
          "to believe that this is a linear trend")

print(linear_regression("toy.csv"))