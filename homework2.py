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


def check(a):
    while a.isnumeric():
        return int(a)
    raise InvalidDataException(message='возраст - это целое число', add_info=a)


def check_data(y, z):
    global d
    try:
        check(y)
        for i in range(len(z)):
            if z[i] == '':
                raise ProcessingException(message='Bы не ввели контрольный вопрос или ответ: ', question=z[0], answer=z[1])
    except InvalidDataException as err_:
        print(f'Ошибка ввода: {err_.message}, а вы ввели - {err_.add_info}')
    except ProcessingException as miss_:
        print(f'Ошибка ввода: {miss_.message}., ваш вопрос - {miss_.question}, ваш ответ - {miss_.answer}')
    else:
        d = True
        print('Ошибок нет')
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
