import math
from sympy import *
import numpy as np

p = symbols('p')
qd = 20 - p
QS = 50 * p - 250
n = 15
Qd = n * qd
print('Суммарный спрос Qd =', Qd)
p0 = solve(Qd - QS, p)
print('Равновесная цена =', p0[0])
qd = qd.subs({p:10})
print('Ответ: каждый из 25 потребителей будет преобретать', qd, 'единиц товара.')