from os.path import exists
from csv_creater import creating
from logger import writing_scv
from logger import writing_xml

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_xml()
