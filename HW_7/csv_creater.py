def creating ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'\nФамилия\tИмя\tОтчество\tДолжность\tНомер телефона\tКомментарий\n')
    file = 'Phonebook.xml'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'\nФамилия\tИмя\tОтчество\tДолжность\tНомер телефона\tКомментарий\n')
