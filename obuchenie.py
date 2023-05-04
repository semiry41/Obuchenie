print('Задание №1')
import math
a = 5
b = 5
perimetr = 4 * a
print('Периметр равен =', perimetr)
ploshad = a ** 2
print('Площадь равна =', ploshad)
diagonal = math.sqrt(a ** 2 ** 0.5)
print('Диагональ равна =', diagonal,'\n')

print('Задание №2')
a = 2
b = 100
c = 3
diskriminant = b ** 2 - 4 * a * c
if diskriminant > 0:
      x1 = (-b + diskriminant ** 0.5) / (2 * a)
      x2 = (-b - diskriminant ** 0.5) / (2 * a)
print('Дискриминант равен', diskriminant)
print('x1= %.2f' % x1)
print('x2= %.2f' % x2,'\n')

print('Задание №3')
stroka_1 = 'Каждый год весна.'
stroka_2 = 'Мы сидели на веранде.'
predlojenie = stroka_1 + stroka_2
print(predlojenie)
stroka_new_1 = stroka_1.replace('Ка','Мы')
stroka_new_2 = stroka_2.replace('Мы','Ка')
print(stroka_new_1,stroka_new_2,'\n')

print('Задание №4')
dir = r'C:\python3\obuchenie.py'
print(dir.rsplit('.', 1)[0])
put = dir.split('\\')
print(dir.split('\\'))
#Название диска
print(put[0])
#Корневая папка
print(put[1])
#Без расширения
print(put[len(put) - 1].split('.')[0],'\n')

print('Задание №5')
a = 5
b = 4
print('{} + {} = {}'.format(a, b, a + b))
print('{} * {} = {}'.format(a, b, a * b),'\n')

print('Задание №6')
stroka = 'abcdef dasasd'
print(stroka[0::2],'\n')

print('Задание №7')
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
index_1 = second_string.find('w')
index_2 = second_string.find('f')
index_3 = second_string.find('t')
sorted_list = [index_1, index_2, index_3]
sorted_list.sort()
print(second_string[sorted_list[0]:sorted_list[2] + 1])