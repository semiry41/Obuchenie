a = 5
b = 20
c = 5
D = b**2 - 4*a*c
print('Дискриминант = ' + str(D))
if D < 0:
    print('Корней нет')
elif D == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1), "%.2f" % x1)
    print('x₂ = ' + str(x2), "%.2f" % x2)