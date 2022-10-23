#Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).
print("ВВедите значение четверти:")
chetvert= int(input())
if chetvert == 1:
    xy= ['x>0,y>0'] 
    print(xy)
if chetvert == 2:
    xy= ['x<0,y>0'] 
    print(xy)
if chetvert == 3:
    xy= ['x<0,y<0'] 
    print(xy)
if chetvert == 4:
    xy= ['x>0,y<0'] 
    print(xy)
    
