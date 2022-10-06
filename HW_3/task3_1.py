#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randrange
n= int(input('n:  '))
list=[randrange(n) for i in range(n)]
sum = 0

print(list, end =' -> ')

print('На нечетных позициях: ', end= '')

for i in range(0, len(list), 2):
    print(list[i], end=' и ' )
    sum+=list[i]
print('ответ: ', sum)
