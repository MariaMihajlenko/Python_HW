# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.20
from inspect import _void
from random import random
import random
from unittest import result

n = int(input('n:  '))
list = []

for i in range(n):
    list.append((random.uniform(0, 10)))
print(list)

res = []
for i in range(n):
    res.append((list[i])-int(list[i]))

print(
    f'\nРазность минимального и максимального значения дробей списка равна: {max(res)-min(res)}')
