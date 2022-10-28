import re
import csv

text_file = open('Phonebook.csv', 'r', encoding='utf-8')
print("\t\t\t\t\tБД к работе готова!!!!\n\n")
print("\t\t\t\tВведите цифру относящуюся к действию:    \n\n")
print("1 - вывод содержимого файла в консоль")
print("2 - добавление данных")
print("3 - удаление данных")
print("4 - редактирование данных")

unit = input()

if unit == "1":  # Вывод на консоль
 print(text_file.read())
text_file.close()


if unit == '2':  # Добавление новой строки
    info = []
    id = input('Введите ID сотрудника:  ')
    info.append(id)
    first_name = input('Введите Фамилию сотрудника:  ')
    info.append(first_name)
    name = input('Введите Имя:  ')
    info.append(name)
    sur_name = input('Введите отчество:  ')
    info.append(sur_name)
    data_born = input('Введите дату рождения :  ')
    info.append(data_born)
    data_work = input('Введите дату приема на работу :  ')
    info.append(data_work)
    position = input('Введите должность:   ')
    info.append(position)
    num_order = input('Введите номер ПРИКАЗА О ПРИЕМЕ НА РАБОТУ:   ')
    info.append(num_order)
    phone_home = ''
    valid = False
    while not valid:
        try:
            phone_home = input('Введите номер телефона: ')
            if len(phone_home) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_home = int(phone_home)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_home)
    phone_work = ''
    valid = False
    while not valid:
        try:
            phone_work = input('Введите Рабочий номер сотрудника: ')
            if len(phone_work) != 3:
                print('В номере телефона должно быть 3 цифры!!!')
            else:
                phone_work = int(phone_work)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_work)
    status = input('Введите статус сотрудника на текущий момент: ')
    info.append(status)

    text_file = 'Phonebook.csv'
    with open(text_file, 'a', encoding='utf-8') as data:
        data.write(
            f'\n{info[0]}\t{info[1]}\t{info[2]}\t{info[3]}\t{info[4]}\t{info[5]}\t{info[6]}\t{info[7]}\t{info[8]}\t{info[9]}\t{info[10]}')
text_file.close()



if unit == '3':  # Удаление строки по фамилии
   str = []
   with open('Phonebook.csv') as f:
    lines = f.readlines()
   str = input('Введите фамилию сотрудника для удаления данных по нему из файла:  ')
   pattern = re.compile(re.escape(str))
   with open('Phonebook.csv', 'w') as f:
      for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)
text_file.close()


if unit == '4':  # Редактирование данных
   print('Редактирует по номеру ID с заменой всей строки.  ')
   f = open('Phonebook.csv', 'r')
   lines = f.readlines()
   i = int(input('Введите ID сотрудника для редактировани:  '))
   j = input('ID;Фамилия;Имя;Отчество;Дата_рождения;Дата_приема;Должность;Номер приказа;Телефон_моб;Телефон_раб;Статус:  ')
   lines[i] = j + '\n'
   save_changes = open('Phonebook.csv', 'w')
   save_changes.writelines(lines)
text_file.close()
 
