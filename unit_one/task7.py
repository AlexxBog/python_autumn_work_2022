#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().
dot_a = float(input("Введите точку А: "))
dot_b = float(input("Введите точку B: "))
dot_c = float(input("Введите точку C: "))
ab = dot_a - dot_b
if ab >= 0:
	print("Расстояние АB: ", ab)
else:
	print("Расстояние АB: ", ab * -1)
bc = dot_b - dot_c
if bc >= 0:
	print("Расстояние BC: ", bc)
else:
	print("Расстояние BC: ", bc * -1)
ab_bc = ab + bc
if ab >= 0:
	print("Сумма отрезков AB и BC", ab_bc)
else:
	print("Сумма отрезков AB и BC", ab_bc * -1)
print("Тип данных ab", type(ab))
print("Тип данных bc", type(bc))
print("Тип данных ab_bc", type(ab_bc))
