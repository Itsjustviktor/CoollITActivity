import numpy as np
import math
from sklearn.preprocessing import StandardScaler

def k_nearest(X, k, obj):
    X_sub = X[:, 0:-1]
    
    # нормализация данных
    scaler = StandardScaler()
    scaler.fit(X_sub)
    X_sub_Mean = scaler.mean_
    X_sub_Std = np.std(X_sub, axis=0)
    for i in range(len(obj)):
        obj[i] = (obj[i] - (np.mean(X_sub, axis=0))[i]) / (np.std(X_sub, axis=0))[i]
    for i in range(X_sub.shape[1]):
        X_sub[:, i] = (X_sub[:, i] - X_sub_Mean[i]) / X_sub_Std[i]

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
