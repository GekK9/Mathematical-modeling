import numpy as np

from numpy import linalg as ln

A = np.array([[-1, 0], [2, 2]])

def f(x):
    return ln.matrix_power(x, 3) + 2 * x -4

print(f(A))