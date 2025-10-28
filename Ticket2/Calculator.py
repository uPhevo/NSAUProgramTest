run = True
while run:
    num = input("Введите выражение (например: 8 + 2): ").split(" ")
    if num[1]=='+':
        print(int(num[0]) + int(num[2]))
    elif num[1] == '/':
        if num[2] != '0':
            print(int((num[0]) / int(num[2])))
        else:
            print("Ошибка деления на ноль")
    else:
        print('Неизвестная операция')
