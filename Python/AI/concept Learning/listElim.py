import numpy as np


def LisElim(X, T):
    X = np.array(X)
    T = np.array(T)
    n = X.shape[1]
    A = []
    for i in range(n):
        A.append(sorted(list((set(X[:, i])))))
    H = []
    t = []
    i = 1
    idx_data = [0]*n
    while True:
        h = []
        for j in range(n):
            h.append(A[j][idx_data[j]])
        for tt in np.unique(T):
            if isConsist(X, T, h, tt):
                H.append(h)
                t.append(tt)
                print(i, h, tt)
                i += 1
        idx_data[-1] += 1
        letter_index = n-1
        while idx_data[letter_index] > len(A[letter_index])-1:
            idx_data[letter_index] = 0
            letter_index -= 1
            if letter_index < 0:
                return H, t
            idx_data[letter_index] += 1
    return H, t


def isConsist(X, T, h, t):
    for i in range(len(X)):
        if h == list(X[i]):
            if T[i] != t:
                return False
    return True


if __name__ == '__main__':
    X = [
        ['sunny', 'warm', 'normal', 'strong', 'warm', 'same'],
        ['sunny', 'warm', 'high', 'strong', 'warm', 'same'],
        ['rain', 'cold', 'high', 'strong', 'warm', 'change'],
        ['sunny', 'warm', 'high', 'strong', 'cool', 'change'],
    ]
    T = ['yes', 'yes', 'no', 'yes']
    H, t = LisElim(X, T)
