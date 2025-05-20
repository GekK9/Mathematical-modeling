import scipy
from scipy.optimize import linprog


A_ub = [[3, 2], [5, 3], [2, 4]]
c = [45, 49, 42]
B_ub = [-5, -9]

A_ub_T = -scipy.transpose(A_ub)
res = linprog(c, A_ub_T, B_ub)

print(res)
