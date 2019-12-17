
import numpy as np

def confusion_matrix(true, pred):
    assert true.shape == pred.shape
    if len(true.shape) != 1:
        true = true.squeeze()
        pred = pred.squeeze()
    uniques = list(np.unique(true))
    uniques += list(np.unique(pred))
    uniques = list(set(uniques))
    cm = np.zeros((len(uniques), len(uniques)), dtype=np.int64)
    for i, l1 in enumerate(uniques):
        for j, l2 in enumerate(uniques):
            cm[i, j] = np.sum((true == l1) * (pred == l2))
        
    return cm

def accuracy(true, pred):
    assert true.shape == pred.shape
    if len(true.shape) != 1:
        true = true.squeeze()
        pred = pred.squeeze()
    return (true == pred).sum()/len(true)



def precision(true, pred):
    cm = confusion_matrix(true, pred)
    #diag_indices = [[i, i] for i in range(len(cm))]
    #tp = cm[diag_indices]
    return (true == pred)*(true ).sum()/len(true)

def recall(true, pred):
    cm = confusion_matrix(true, pred)
### F score

def f1(true, pred):
    def __init__(self):
        