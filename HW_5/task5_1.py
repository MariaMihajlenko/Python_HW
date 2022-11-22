#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import re

s= 'голос слух осязание понимание речь автор абривиатура опера бра' 
words = s.split()
words = re.split('\W+', s)
ex = ['a','б','в']

print(words) 

for i in range(len(words)-1,-1,-1):
    if words[i].find(ex[0])!=-1 or words[i].find(ex[1])!=-1 or words[i].find(ex[2])!=-1:
        del words[i]
print(*words)