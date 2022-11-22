#Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]
import itertools

lst_input = input('Введите последовательность чисел :  ')
lst_number = [int(num)for num in lst_input.split()]
lst_not_doble = list(set(lst_number))
lst_sort = sorted(lst_number)
lst_unique = []
lst_repeat = []
for num, lst_num in itertools.groupby(lst_sort):
    if len(list(lst_num)) ==1:
        lst_unique.append(num)
    else:
        lst_repeat.append(num)   
print(f'Исходная последовательность чисел:   {lst_number}')   
print(f'Список неповторяющихся чисел:   {lst_unique}')  
print(f'Список повторяющихся чисел последовательности:   {lst_repeat}')  
print(f'Список без дублей:   {lst_not_doble}')     







