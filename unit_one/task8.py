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

a = int(input('Введите А '))
b = int(input('Введите Б '))
c = int(input('Введите С '))
if a >= b and a >= c and b >= c:
    print(c, a, b)
elif a >= b and a >= c and b <= c:
    print(b, c, a)
elif b >= a and b >= c and a >= c:
    print(c, a, b)
elif b >= a and b >= c and a <= c:
    print(a, c, b)
elif c >= a and c >= b and a >= b:
    print(b, a, c)
elif c >= a and c >= b and a <= b:
    print(a, b, c)


