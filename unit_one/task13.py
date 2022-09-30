#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.
mass = list(range(-21, -11))
print(mass)
it = 0
for i in mass:
    mass[it] = i + 1
    it = it + 1
print(mass)