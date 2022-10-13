# Реализуйте RLE алгоритм: реализуйте модель сжатия и восстановления данных.
# Входные и выходные данные храняться в отдельных текстовых файлах.

with open('textinput.txt','r') as data:
    count = 0
    a = data.read()
    for i in range(len(a)-1):
        if i <= len(a):
            if a[i] == a[i+1]:
                count+=1
        else:
            print(f'{count}{a[i]}' , end='')
count = 1
print(f'{count},{a[i]}')
a='3w'
b = ''
for i in range(0,len(a),2):
    if i <= len(a):
       c = int(a[i])
b+=a[i+1]*c

with open('textout.txt' , 'a') as data:
    data.write(b)

    