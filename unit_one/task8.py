#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
#a = 10
#b = 3
#c = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
#A = 2
#B = 10
#C = 7
# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10

a = 10
b = 3
c = 7

if a > b and a > c and b > c:
    a_1 = a
    a = c
    c = a_1
    print('A = ', a)
    print('B = ', b)
    print('C = ', c)
elif a > b and a > c and b < c:
    a_1 = a
    a = b
    b = c
    c = a_1
    print('A = ', a)
    print('B = ', b)
    print('C = ', c)
elif b > a and b > c and a > c:
    a_1 = a
    a = c
    c = b
    b = a_1
    print('A = ', a)
    print('B = ', b)
    print('C = ', c)
elif b > a and b > c and c > a:
    b_1 = b
    b = c
    c = b_1
    print('A = ', a)
    print('B = ', b)
    print('C = ', c)
elif c > a and c > b and a > b:
    z = a
    a = b
    b = z
    print('A = ', a)
    print('B = ', b)
    print('C = ', c)
elif c > a and c > b and b > a:
    print('A = ', a)
    print('B = ', b)
    print('C = ', c)
