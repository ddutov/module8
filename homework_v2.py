# -*- coding: utf-8 -*-
def check_float(var_str):
    for char in var_str:
        if not 48 <= ord(char) <= 57 and ord(char) != 46:
            return var_str
    var_str = float(var_str)
    return var_str


def check_int(var_str):
    for char in var_str:
        if not 48 <= ord(char) <= 57:
            return var_str
    var_str = int(var_str)
    return var_str


def add_everything_up(a, b):
    try:
        s = a + b
        print('Складываем если переменные числа или строки. Ответ:')
    except TypeError:
        s = str(a) + str(b)
        print('Нельзя складывать строки с числами! Можно просто склеить их вот так:')
    return s


while True:
    var_1 = input('Введите переменную a: ')
    var_2 = input('Введите переменную b: ')
    var_1 = check_int(var_1)
    if isinstance(var_1, int) is False:
        var_1 = check_float(var_1)
    var_2 = check_int(var_2)
    if isinstance(var_2, int) is False:
        var_2 = check_float(var_2)
    print(add_everything_up(var_1, var_2))
