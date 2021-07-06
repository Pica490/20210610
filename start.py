import csv
from correct_name import name
from correct_pattern import correct_pattern

with open(r'C:\Users\kuzne\Desktop\Python\pythonProject5\raw_data\phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contact_list = list(rows)

list_phonebook = name(contact_list)
list_phonebook_new = correct_pattern(list_phonebook)
print(list_phonebook_new)

with open("phonebook.csv",  "w",encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(list_phonebook_new)

