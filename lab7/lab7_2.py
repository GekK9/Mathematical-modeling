import numpy as np
from numpy import linalg

A = np.array([[0, 1], [16, 1]])
B = np.array([30, 16])
X = np.linalg.solve(A, B)
for b,a in zip(X, ['a =', 'b =',]):
    print(a, b)
print('Ответ: количество домов y =', -2, 'x +', b,', где x количество кораблей')

