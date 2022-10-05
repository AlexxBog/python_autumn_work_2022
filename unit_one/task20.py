#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().


#Содержимое файла import_this.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

#выходные данные
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.

file = open("import_this.txt", "wt")
file.write("Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\n")
file.close()

file = open("import_this.txt", "rt")
mass = file.readlines()
rev = mass[::-1]
for i in rev:
    print(i, end="\r")
file.close()









