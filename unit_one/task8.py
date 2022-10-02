#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
a = 10
b = 3
c = 7
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
    print('A = ', c)
    print('B = ', b)
    print('C = ', a)
elif a > b and a > c and b < c:
    print('A = ', b)
    print('B = ', c)
    print('C = ', a)
elif b > a and b > c and a > c:
    print('A = ', c)
    print('B = ', a)
    print('C = ', b)
elif b > a and b > c and c > a:
    print('A = ', a)
    print('B = ', c)
    print('C = ', b)
elif c > a and c > b and a > b:
    print('A = ', b)
    print('B = ', a)
    print('C = ', c)
elif c > a and c > b and b > a:
    print('A = ', a)
    print('B = ', b)
    print('C = ', c)
