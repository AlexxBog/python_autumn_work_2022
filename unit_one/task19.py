#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#Каждое значение из списка должно находится на отдельной строке.
fail = open("algoritm.csv", "wt")
id = 0
for i in algoritm:
    id+=1
    strid = str(id)
    fail.write("id" + strid + ' ' + i + "\n")
fail.close()









