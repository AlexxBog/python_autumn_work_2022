#Преобразуйте переменную age и foo в число 
age = "23"
age = int(age)
foo = "23abc"
# Переменную foo нельзя преобразовать в тип int
#Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)
#Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
#Преобразуйте значение  в Boolean
str_one = "Privet"
str_one = bool(str_one)
str_two = ""
str_two = bool(str_two)
#Преобразуйте значение 0 и 1  в Boolean
a = 0
b = 1
a = bool(a)
b = bool(b)
print(a)
print(b)