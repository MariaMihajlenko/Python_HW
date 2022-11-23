
import re
import csv

"""
This is a echo bot.
It echoes any incoming text messages.
"""
import logging
import csv
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = ''
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
text_file = open('Phonebook.csv', 'r', encoding='utf-8')
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    БД к работе готова!!!!
Введите цифру относящуюся к действию:    
"/1 - вывод содержимого файла в консоль"
"/2 - добавление данных"
"/3 - удаление данных"
"/4 - редактирование данных"
    """
    await message.reply("Hi!\nБД к работе готова!!!!\nВведите цифру относящуюся к действию:\n1 - вывод содержимого файла в консоль\n2 - добавление данных\n3 - удаление данных\n4 - редактирование данных")


@dp.message_handler(commands=['1'])
async def comm_1(message: types.Message):
     await message.reply('Вывод данных в консоль:  ')
     await message.reply(text_file.read())



@dp.message_handler(commands=['2'])
async def comm_2(message: types.Message):
    text_file = open('Phonebook.csv', 'r', encoding='utf-8')
    info = []
    await message.reply('Добавление сотрудника в БД:  ')
    

    await message.reply('Введите ID сотрудника:  ')
    id = input(message.text)
    info.append(id)
    await message.reply('Введите Фамилию сотрудника:  ')
    first_name = input()
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




@dp.message_handler(commands=['3'])
async def comm_3(message: types.Message):
     
   await message.reply('Удаление данных из  БД:  ')  
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



@dp.message_handler(commands=['4'])
async def comm_4(message: types.Message):
   await message.reply('Редактирует по номеру ID с заменой всей строки.  ')
   f = open('Phonebook.csv', 'r')
   lines = f.readlines()
   i = int(input('Введите ID сотрудника для редактировани:  '))
   j = input('ID;Фамилия;Имя;Отчество;Дата_рождения;Дата_приема;Должность;Номер приказа;Телефон_моб;Телефон_раб;Статус:  ')
   lines[i] = j + '\n'
   save_changes = open('Phonebook.csv', 'w')
   save_changes.writelines(lines)

 
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)