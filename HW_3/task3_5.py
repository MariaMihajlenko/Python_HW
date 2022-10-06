#Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
from tokenize import Double


n = int(input('Введите любое число:  '))
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(10))
print(data)