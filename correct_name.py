def double(current_values, new_values):

  for i in range(5):
    if (current_values [i] == '' and new_values[i] !=''):
      current_values[i] = new_values[i]
  return (current_values)

def checking(lastname, firstname, surname, values, a):
  if (lastname, firstname) not in a:
    a[(lastname, firstname)] = values
    a[(lastname, firstname)][0] = surname

  else:
    current_values = a[(lastname, firstname)]
    double(current_values, values)
    a[(lastname, firstname)] = current_values

def name(list):
  a = {}

  for value in list:

    record = value[0].split(' ')
    record2 = value[1].split(' ')
    lastname = record[0]

    if len(record) == 3:
      firstname = record[1]
      surname = record[2]

    elif len(record) == 2:
      firstname = record[1]
      surname = value[2]

    elif len(record) == 1:
      if len(record2) == 1:
        firstname = (value[1].split(' '))[0]
        surname = value[2]
      else:
        firstname = (value[1].split(' '))[0]
        surname = (value[1].split(' '))[1]

    checking(lastname, firstname, surname, value[2:7], a)

  list_phonebook = []
  for key, value in a.items():
     list_phonebook.append([key[0],key[1],value[0], value[1], value[2], value[3], value[4]])

  return list_phonebook











