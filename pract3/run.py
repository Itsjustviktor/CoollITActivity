import numpy as np
import matplotlib.pyplot as plt
from pract3.k_means import kmeans



# евклидово расстояние между двумя точками
def dist(A, B):
  r = np.sqrt(np.sum((A-B)**2))
  return r

# расстояние городских кварталов
def dist_function(A, B):
  r = np.sum(abs(A-B))
  return r


# исходные данные
X = np.array([
  [4, 4],
  [3, 3],
  [5, 3],
  [5, 4],
  [2, 2]])

# запуск кластеризации
ans = kmeans(2, X, dist)
[2, 3],
[5, 5],
[3, 2],
[2, 4],
[4, 5],
# отображение результатов
print(ans)
plt.plot(X[:,0], X[:,1], 'bx', ans[:,0], ans[:,1], 'r*', markersize=20)
plt.grid()
plt.show()



# запуск кластеризации
ans2 = kmeans(2, X, dist_function)
[2, 3],
[5, 5],
[3, 2],
[2, 4],
[4, 5],
# отображение результатов
print(ans)
plt.plot(X[:,0], X[:,1], 'bx', ans2[:,0], ans2[:,1], 'r*', markersize=20)
plt.grid()
plt.show()
