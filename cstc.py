from repeat import repeat
import math

def cstc():
    operation = {
        "sin" : math.sin,
        "cos" : math.cos,
        "tan" : math.tan,
        "atan" : math.atan
    }
    while True\
            :
        try:
            oper = input("   Введите операцию(sin, cos, tan, atan) >>> ")
            oper = oper.replace(" ", "")
            geom_num = float(input("Введите обрабатываемое число >>> "))
            print(operation[oper](geom_num))
        except ValueError:
            print('невернный ввод.')
            print('Попробуйте ище раз.\n'
                  '------------------------------\n')
            continue
        else:
            flag = 0
        if not repeat():
            print('Виход...')
            break
