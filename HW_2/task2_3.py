#Задайте список из n чисел последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.

print('Введите N:   ')
n = int(input())
def counter(n):
  return[round((1+1/x)**x,2) for x in range(1,n+1)]
print(counter(n))
print(round(sum(counter(n))))


