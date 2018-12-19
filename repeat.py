def repeat():  #ф-ция повторение последнего действия
    while True:
        cont = input('''
        Вы хотите использовать калькулятор повторно:\n
        "Y" - да, "N" - нет
        ''')
        while cont.lower() in ("yes", "y", "н", "нуы", "да", "д"):
            return True
        if cont.lower() in ("no", "n", "т", "тщ", "нет", "н"):
            return False
        else:
            print('невернный ввод.')
