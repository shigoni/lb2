import random

a = int(input("Введите номер задания (1-4):  "))

if a == 1:
    p1 = input("Введите пароль: ")
    p2 = input("Повторите пароль: ")
    if p1 == p2:
        print("Пароль принят")
    else:
        print("Пароль не принят")
elif a == 2:
    nmesta = int(input("Введите номер места (0-55): "))
    if 0 < nmesta < 55:
        if nmesta % 2 == 0:
            print("Верхнее")
        else:
            print("Нижнее")
    else:
        print("Нет такого места")
elif a == 3:
    got = int(input("Введите год (####): "))
    if got % 4 == 0 and got % 100 != 0 or got % 400 == 0:
        print("Год", got, "- високосный")
    else:
        print("Это год не високосный")
elif a == 4:
    cvet = ['красный', 'жёлтый', 'синий']
    cvet1 = random.choice(cvet)
    cvet2 = random.choice(cvet)
    print ("Цвет 1: ", cvet1, "| Цвет 2: ", cvet2)
    print("Смесь: ")
    if cvet1 == cvet2:
        print(cvet1)
    elif cvet1 == "красный" and cvet2 == "синий" or cvet2 == "красный" and cvet1 == "синий":
        print("фиолетовый")
    elif cvet1 == "красный" and cvet2 == "жёлтый" or cvet2 == "красный" and cvet1 == "жёлтый":
        print("оранжевый")
    elif cvet1 == "синий" and cvet2 == "жёлтый" or cvet2 == "синий" and cvet1 == "жёлтый":
        print("зелёный")
