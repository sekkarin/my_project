import numpy as np

def KNN(Xtrain,Ytrain,Xtest,k):
    Ytrain = []
    for x in Xtest :
        d = np.sqrt(np.sum((Xtrain - x) ** 2,axis = 1))
        idx = np.argsort(d)
        (values,counts) = np.unique(Ytrain[idx[:k]],retrue_counts = True)
        ind = np.argmax(counts)
        Ytrain.append(values[ind])
    return Ytrain