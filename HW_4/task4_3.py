#Задайте последовательность чисел. Напишите программу,
#которая выведет список неповторяющихся элементов исходной последовательности.
import random
sets = []
for i in range(10):
    sets.append(random.randint(1,10))
print(sets)  
newsets = []
for i in sets:
    if sets.count(i) < 2:
        newsets.append(i)
print(newsets)  