import re

def correct_pattern(list_phonebook):
    print(list_phonebook)
    pattern_phone = r"(8|\+7)\s?(\(?(...)\)?|)(\s|-)?(...)[-]?(..)[-]?(\d+)"
    sub = r"+7(\3)\5-\6-\7"

    pattern_phone2 = r'\(?(доб.)\s(\d+)\)?'
    sub2 = r'\1\2'

    list_phonebook_new = [list_phonebook[0]]
    for i in range(len(list_phonebook)-1):
        result = re.sub(pattern_phone, sub, list_phonebook[i+1][5])
        result2 = re.sub(pattern_phone2,sub2, result)
        list_phonebook_new.append([list_phonebook[i+1][0],list_phonebook[i+1][1], list_phonebook[i+1][2],list_phonebook[i+1][3],list_phonebook[i+1][4], result2, list_phonebook[i+1][6]])

    return (list_phonebook_new)






