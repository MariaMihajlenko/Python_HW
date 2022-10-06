#Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
from random import randrange

n= int(input('n:  '))
list=[randrange(n) for i in range(n)]
print(list, end=' ,')

x =len(list)

for i in range(0, x):
 p = list[i]*list[x-i-1]
 print(p, end=' ,')
 i+=i 
 
 if i > (x%2+1):
  break 
     
