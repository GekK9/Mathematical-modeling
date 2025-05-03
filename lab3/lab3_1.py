from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
R = np.abs(np.sqrt(np.sin(Y)**2 + 6.835) + np.exp(X))

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, R, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('R')
ax.set_title('$R = | \sqrt{\sin^2 y + 6.835} + e^x |$')
plt.show()