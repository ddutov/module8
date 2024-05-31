# -*- coding: utf-8 -*-

def check_float(str):
    for char in str:
        if not 48 <= ord(char) <= 57 and ord(char) != 46:
            return str
    str = float(str)
    return str

def check_int(str):
    for char in str:
        if not 48 <= ord(char) <= 57:
            return str
    str = int(str)
    return str


def add_everything_up(a, b):
    if isinstance(a, str) and isinstance(b, str):
        s = a + b
    elif isinstance(a, str):
        s = a + str(b)
    elif isinstance(b, str):
        s = b + str(a)
    else:
        s = a + b
    return s


while True:
    var_1 = input('Введите переменную a: ')
    var_2 = input('Введите переменную b: ')
    var_1 = check_int(var_1)
    if isinstance(var_1,int) is False:
        var_1 = check_float(var_1)
    var_2 = check_int(var_2)
    if isinstance(var_2,int) is False:
        var_2 = check_float(var_2)
    print(add_everything_up(var_1, var_2))
