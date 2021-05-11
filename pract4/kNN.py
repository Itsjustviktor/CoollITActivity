import numpy as np
import math

def k_nearest(X, k, obj):
    X_sub = X[:, 0:-1]

    a = [dist(i, obj) for i in X_sub]
    h = np.argsort(a)
    h = h[:k]
    nearest_classes = X[h, -1]
    unique, counts = np.unique(nearest_classes, return_counts=True)

    object_class = unique[np.argmax(counts)]

    return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))
