import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

def get_data_loader(training = True):

    custom_transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])

    train_set=datasets.FashionMNIST('./data',train=True,
            download=True,transform=custom_transform)
    test_set=datasets.FashionMNIST('./data', train=False,
            transform=custom_transform)

    data_set = train_set
    if (training == False):
        data_set = test_set

    loader = torch.utils.data.DataLoader(data_set, batch_size = 64)

    return loader

def build_model():

    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(784, 128),
        nn.ReLU(),
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Linear(64, 10)
    )

    return model

def train_model(model, train_loader, criterion, T):
    """
    INPUT:
        model - the model produced by the previous function
        train_loader  - the train DataLoader produced by the first function
        criterion   - cross-entropy
        T - number of epochs for training

    RETURNS:
        None
    """

    opt = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    model.train()

    for epoch in range(T):
        running_loss = 0.0
        correct = 0
        n = 0
        for image, labels in train_loader:
            outputs = model(image)
            opt.zero_grad()
            loss = criterion(outputs, labels)
            loss.backward()
            opt.step()
            _, predicted = torch.max(outputs.data, 1)
            running_loss += loss.item()
            correct += (predicted == labels).sum().item()
            n += labels.size(0)
            if (n == 60000):
                print("Train Epoch: {:d} Accuracy: {:d}/{:d}({:.2f}%) Loss: {:.3f}"
                        .format(epoch, correct, n, 100*(correct/n), running_loss/len(train_loader)))

    return

def evaluate_model(model, test_loader, criterion, show_loss = True):
    """
    INPUT:
        model - the trained model produced by the previous function
        test_loader    - the test DataLoader
        criterion   - cropy-entropy

    RETURNS:
        None
    """
    model.eval()
    running_loss = 0.0
    correct = 0
    n = 0
    with torch.no_grad():
        for data, labels in test_loader:
            outputs = model(data)
            loss = criterion(outputs, labels)
            _, predicted = torch.max(outputs.data, 1)
            running_loss += loss.item()
            correct += (predicted == labels).sum().item()
            n += labels.size(0)
        if show_loss:
            print("Average loss: {:.4f}".format(running_loss/n))
        print("Accuracy: {:.2f}%".format(100*(correct/n)))

def predict_label(model, test_images, index):
    """
    INPUT:
        model - the trained model
        test_images   -  test image set of shape Nx1x28x28
        index   -  specific index  i of the image to be tested: 0 <= i <= N - 1


    RETURNS:
        None
    """
    class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt'
                ,'Sneaker','Bag','Ankle Boot']
    probs = []
    logits = model(test_images)
    prob = F.softmax(logits, dim=1)

    for i in range(len(class_names)):
        probs.append((class_names[i], prob[index][i].item() * 100))
    probs.sort(key=lambda el: el[1], reverse=True)

    for i in range(3):
        print("%s: %.2f%%" % (probs[i][0], probs[i][1]))

if __name__ == '__main__':
    '''
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    '''
    criterion = nn.CrossEntropyLoss()

    train_loader = get_data_loader()
    test_loader = get_data_loader(False)
    model = build_model()
    train_model(model, train_loader, criterion, T = 5)
    evaluate_model(model, test_loader, criterion, show_loss = True)
    data_iter = iter(test_loader)
    images, labels = data_iter.next()
    pred_set = images
    predict_label(model, pred_set, 1)
