first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
index_1 = second_string.find('w')
index_2 = second_string.find('f')
index_3 = second_string.find('t')
sorted_list = [index_1, index_2, index_3]
sorted_list.sort()
print(second_string[sorted_list[0]:sorted_list[2] + 1])