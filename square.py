from repeat import repeat


def square():
    import math
    while True:
        try:
            answer = float(input("Введите число для поиска квадратного корня: "))
            if answer > 0 or answer < 0:
                print(math.sqrt(answer))
            elif answer == 0:
                print('0.0')
            if not repeat():
                print('Square exit')
                break
        except (ZeroDivisionError, ValueError) as error:
            print('\nОШИБКА: ', error, '\n')
            print('Попробуйте ище раз.\n'
                  '------------------------------\n')
