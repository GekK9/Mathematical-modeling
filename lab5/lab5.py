from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

c = np.array([5, 9])
A = np.array([[4, 3], [2, 5], [4, 2]])
B = np.array([45, 45, 29])

res = optimize.linprog(-c, A, B)

print(res)

x = np.linspace(0, 8.5, 50)
y1 = (45 - 4*x) / 3
y2 = (45 - 2*x) / 5
y3 = (29 - 4*x) / 2


plt.title("Р—Р°РІРёСЃРёРјРѕСЃС‚СЊ:")
plt.xlabel("x1")
plt.ylabel("x2")

plt.grid()
plt.plot(x, y1, x, y2, x, y3)
plt.show()