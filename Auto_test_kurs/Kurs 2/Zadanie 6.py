string1 = 'Шла Саша по шоссе и сосала сушку'
string2 = ''
for i in range(len(string1)):
    if i % 2 == 0:
        string2 += string1[i]
print(string2)