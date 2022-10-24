from user_interface import get_info as gi

info = gi()
def writing_scv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'\n{info[0]}\t{info[1]}\t{info[2]}\t{info[3]}\t{info[4]}\t{info[5]}\n')

def writing_xml ():
   file = 'Phonebook.xml'
   with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'\n{info[0]}\t{info[1]}\t{info[2]}\t {info[3]}\t {info[4]}\t {info[5]}\n')
