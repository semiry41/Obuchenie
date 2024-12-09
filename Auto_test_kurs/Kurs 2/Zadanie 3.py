string1 = 'Мама мыла раму'
string2 = 'Вася пошел за водой'
print(string1.replace(string1[:2], string2[:2]) + ' ' + (string2.replace(string2[:2], string1[:2])))