import numpy as np

def dist(A, B):
  # Для вычисления квадратного корня используйте функцию np.sqrt
  r = np.sqrt(np.sum((A-B)**2))
  return r


# возвращает список индексов ближайших центров по каждой точке
def class_of_each_point(X, centers):
  m = len(X)
  k = len(centers)

  # матрица расстояний от каждой точки до каждого центра
  distances = np.zeros((m, k))
  for i in range(m):
    for j in range(k):
      distances[i, j] = dist(centers[j], X[i])

  # поиск ближайшего центра для каждой точки
  return np.argmin(distances, axis=1)


def kmeans(k, X):
  m = X.shape[0]  # количество строк в матрице X
  n = X.shape[1]  # количество столбцов в матрице X
  curr_iteration = prev_iteration = np.zeros(m)

  centers =(np.max(X, axis=0) - np.min(X, axis=0)) * np.random.random((k, n)) + np.min(X, axis=0)

  # приписываем каждую точку к заданному классу
  curr_iteration = class_of_each_point(X, centers)
  while np.any(prev_iteration != curr_iteration):
    prev_iteration = curr_iteration
    
    # вычисляем новые центры масс
    for i in range(k):
      sub_X = X[curr_iteration == i,:]
      if len(sub_X) > 0:
        centers[i,:] = np.mean(sub_X, axis=0)

    # приписываем каждую точку к заданному классу
    curr_iteration = class_of_each_point(X, centers)
  
  return centers
