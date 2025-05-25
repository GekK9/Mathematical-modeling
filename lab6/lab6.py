import numpy
from scipy.optimize import linprog


A_ub = [[4, 3], [2, 5], [4, 2]]
c = [45, 45, 29]
B_ub = [-5, -9]

A_ub_T = -numpy.transpose(A_ub)
res = linprog(c, A_ub_T, B_ub)

print(res)
