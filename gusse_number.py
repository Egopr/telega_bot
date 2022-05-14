import random
print('Рады приветствовать на игре угадай загаданное число')
start = int(input('1. Новая игра\n2. Загрузить игру\n=>'))
if start == 1:
    print ('Компьютер загодал число от 1 до 100, попробуй угадать его')
    print ('при нажатие "S" выполниться вход в меню')
    number = 0
    ran = random.randint(1,101)
    while number != ran:
        number = input('Введите число => ')
        if number.isdigit():
            number = int(number)
            if number > ran:
                print ('число меньше, чем вы написали')
                continue
            elif number < ran:
                print ('число больше, чем вы написали')
                continue
            elif number == ran :
                print ('Вы красавчик вы угадали !!! это число - ', ran)
                break
        elif 'S' == number:
            menu = int(input('1. Продолжить игру\n2. Cохранить игру\n3. Сохранить и выйти\n=> '))
            if menu == 1:
                continue
            elif menu == 2:
                print('Игра сохранена')
                continue
            elif menu == 3:
                break

        else:
            print ('не верное значение')
            continue
elif start == 2:
    print('Варианты сохранений')
else:
    print('Нет такого пункта меню')
