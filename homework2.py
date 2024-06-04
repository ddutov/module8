# -*- coding: utf-8 -*-

class InvalidDataException(Exception):
    def __init__(self, message, add_info):
        self.message = message
        self.add_info = add_info


class ProcessingException(Exception):
    def __init__(self, message, question, answer):
        self.message = message
        self.question = question
        self.answer = answer


def check(a, b):
    while a.isnumeric():
        for i in range(len(b)):
            if b[i] == '':
                raise ProcessingException(message='Bы не ввели контрольный вопрос или ответ: ', question=b[0], answer=b[1])
        return int(a), b
    raise InvalidDataException(message='возраст - это целое число', add_info=a)


def check_data(y, z):
    global d
    try:
        check(y, z)
        d = True
        return d
    except InvalidDataException as err_:
        print(f'Ошибка ввода: {err_.message}, а вы ввели - {err_.add_info}')
    except ProcessingException as miss_:
        print(f'Ошибка ввода: {miss_.message}., ваш вопрос - {miss_.question}, ваш ответ - {miss_.answer}')
    return d


d = False
while d is False:
    name = input('Введите Ваше имя: ')
    years = input('Введите Ваш возраст: ')
    que_ = input('Введите контрольный вопрос: ')
    ans_ = input('введите ответ на контрольный вопрос: ')
    couple = [que_, ans_]
    check_data(years, couple)
print(f'Данные введены правильно: {name} - {years} лет. Регистрация заввершена.')
