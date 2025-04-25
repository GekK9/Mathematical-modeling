import numpy as np
from numpy import linalg as ln

A = np.array([[-1, 0, 8, 6, -1, 5], [8, 4, -5, 4, -5, 11], [3, 6, -14, 7, 8, -2], [10, 4, 0, -4, -2, -6], [-6, -3, -4, -2, 2, 13], [-7, 8, 12, -4, 9, -5]])
print(ln.inv(A))