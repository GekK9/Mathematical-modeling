import numpy as np
from numpy import linalg as ln
a = np.array([[-2, 1, 6], [1, -2, -1], [3, 4, -2]])
b = np.array([0, 5, 13])

x = np.linalg.solve(a, b)

for t, x in zip(x, ['x =', 'y =', 'z = ']):
    print(x, t)


det = np.linalg.det(a)
a_inv = np.linalg.inv(a)
X = np.dot(a_inv, b)
print(X)
    