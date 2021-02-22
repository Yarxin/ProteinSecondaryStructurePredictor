import numpy as np
from model import window_size
import tensorflow as tf


def PrepareData(model_list):
    X_set = str()
    Y_set = str()
    for item in model_list:
        X_set += item.sequence
        Y_set += item.secondary_structure

    return X_set, Y_set

def split_dataset(Dataset, seed=None):
    np.random.seed(seed)
    np.random.shuffle(Dataset)
    train_split = int(Dataset.shape[0]*0.8)
    test_val_split = int(Dataset.shape[0]*0.1)
    Train = Dataset[0:train_split, :, :]
    Test = Dataset[train_split:train_split+test_val_split, :, :]
    Validation = Dataset[train_split+test_val_split:, :, :]
    return Train, Test, Validation

def SplitDataX(X_set):
    train_split = int(X_set.shape[0] * 0.8)
    test_val_split = int(X_set.shape[0] * 0.1)

    X_train = X_set[0:train_split, :]
    X_test = X_set[train_split:train_split + test_val_split, :]
    X_val = X_set[train_split + test_val_split:, :]

    return X_train, X_test, X_val


def SplitDataY(Y_set):
    train_split = int(Y_set.shape[0] * 0.8)
    test_val_split = int(Y_set.shape[0] * 0.1)

    Y_train = Y_set[0:train_split, :]
    Y_test = Y_set[train_split:train_split + test_val_split, :]
    Y_val = Y_set[train_split + test_val_split:, :]

    return Y_train, Y_test, Y_val

def ReshapeDataX(X_set):
    X = np.array([])
    # X = X_set[:, np.newaxis, :]
    lista_poziom1 = []
    lista = []

    i = 0
    while i < len(X_set):
        lista_poziom2 = []
        j = 0
        k = i

        while j < window_size:
            lista_poziom2.append(X_set[k])
            j += 1
            if k == len(X_set) - 1:
                k = 0
            else:
                k += 1
            proc = k / len(X_set) * 100
            print('Procent przetworzonych danych: ' + str(proc) + ' %')
        lista_poziom1.append(lista_poziom2)
        X = np.asarray(lista_poziom1)
        i += 1
    return X



