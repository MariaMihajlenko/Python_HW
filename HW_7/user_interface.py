
def get_info():
    info = []
    last_name = input('Введите фамилию:  ')
    info.append(last_name)
    first_name = input('Введите имя:  ')
    info.append(first_name)
    middle_name = input('Введите отчество:  ')
    info.append(middle_name)
    position = input('Введите должность:   ')
    info.append(position)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    comment = input('Введите комментарий: ')
    info.append(comment)
    return info
