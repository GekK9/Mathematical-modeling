from numpy.random import default_rng
import random
import numpy as np

print('Генерация случайных чисел и последовательностей средвами модуля RANDOM: ')

print(random.random())
print(random.uniform(50, 52))
print(random.gauss(0, 10))

rng = default_rng()
vals = rng.standard_normal(3)
print('Массив из 3ех случайных чисел: ', vals)

print('Повтор псевдослучайных последовательностей: ')
random.seed(1)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())

print('Генерация случайных чисел и последовательностей средствами модуля NUMPY.RANDOM: ')
np.random.seed(1)
print(np.random.rand())
print(np.random.rand())
np.random.seed(1)
print(np.random.rand())

print('Задача о разноцветных шарах: ')
green_ball_count = 0
for i in range (0, 100):
    new_ball = random.choice(['green', 'red', 'red', 'red', 'red'])
    if new_ball == 'green':
        green_ball_count += 1
print(green_ball_count)

print('Задача о монетке: ')
H_count = 0
for i in range(0, 10000):
    new_flip = random.choices(['H', 'T'], weights=[0.2, 0.8])
    if new_flip == ['H']:
        H_count += 1
print(H_count)

print('Моя задача')
balls_count = 0
for i in range (0, 100):
    new_ball = random.choice(['green', 'green', 'green', 'red', 'yellow' , 'red', 'red', 'red', 'blue', 'blue'])
    if new_ball == 'yellow' or new_ball == 'red':
        balls_count += 1
print(balls_count)
