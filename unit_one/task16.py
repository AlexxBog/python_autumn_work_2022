#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
чтобы каждая функция выполняла одно универсальное действие.

def tablo():
    global letter
    if ("".join(answer)) == secret and lives > 0:
        print("\n", " ".join(answer))
        print("Игра окончена\nПоздравляем!!! Вы угадали загаданно слово")
    elif lives == 0:
        print("\nК сожалению, вы проиграли! ((")
        print("Загаданное слово было:", secret)
    else:
        print("\n", " ".join(answer))
        letter = input("Введите букву: ")


def life(live):
    global lives
    lives = live - 1
    print("Нет такой буквы. Вращайте барабан. У вас осталось ", lives, "попыток!")


def serch(word, symbol):
    global answer

    if list(word).count(symbol) == 1:
        ind = list(word).index(symbol)
        answer[ind] = symbol

    else:
        start = 0
        for n in range(list(word).count(symbol)):
            ind = list(word).index(symbol, start, len(word))
            start = ind + 1
            answer[ind] = symbol



pik = random.randint(0, len(words)-1)
secret = words[pik]
print(desc_[pik])

answer = list("X"*len(words[pik]))


while ("".join(answer)) != secret and lives > 0:
    tablo()
    if letter not in secret:
        life(lives)
    else:
        serch(secret, letter)
tablo()
