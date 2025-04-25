import numpy as np
from numpy import linalg as ln

A = np.array([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]])


print(ln.det(A))