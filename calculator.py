from repeat import repeat



def add(number_1, number_2):
    return number_1 + number_2


def sub(number_1, number_2):
    return number_1 - number_2


def div(number_1, number_2):
    return number_1 / number_2


def mul(number_1, number_2):
    return number_1 * number_2


OPERATION = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mul
}


def calculator():
    while True:
        try:
            num_1 = float(input('Введите 1е число: '))
            operation = input('Действие: ')
            operation = operation.replace(' ', '')
            num_2 = float(input('Введите 2е число: '))
            result = None
            result = OPERATION[operation](num_1, num_2)
            print(num_1, operation, num_2, '=', result)
            if not repeat():
                break
        except (ZeroDivisionError, ValueError) as error:
            print('\nОШИБКА: ', error, '\n')
            print('Попробуйте ище раз.\n'
                  '------------------------------\n')
        except KeyError:
            print('невернный ввод.')
            print('Попробуйте ище раз.\n'
                  '------------------------------\n')
