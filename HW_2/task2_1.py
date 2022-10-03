#Напишите программу, которая принимает на вход 
#вещественное число и показывает сумму его цифр. 
from unicodedata import digit
print("Введите вещественное число:  ")
a = str(input())
a = a.replace('-', '').replace('.', '')
a = int (a)
i=0 
sum= 0
while a > 0:
 digit = a % 10
 sum= sum+digit
 a = a //10
print('Сумма элементов числа равна:   ',sum)


