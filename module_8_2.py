collection = []


def personal_sum(numbers):
    a = list(numbers)
    result = 0
    incorrect_data = 0
    for i in range(len(a)):
        try:
            # print('numbers = ', a)
            # print('len numbers = ', len(a))
            # print('i = ', i)
            result += a[i]
        except TypeError as exc:
            print('Некорректный тип данных для подсчёта суммы - ', numbers[i] )
            incorrect_data += 1
    per_sum = (result, incorrect_data)
    # print('per_sum = ', per_sum)
    return per_sum


def calculate_average(data):
    try:
        var_1 = personal_sum(data)
        a = list(data)
        if len(a) == var_1[1] and len(a) != 0:
            average = 0
            return average
        else:
            average = var_1[0] / (len(a) - var_1[1])
            return average
    except ZeroDivisionError:
        print('Нулевая коллекция')
        average = 0
        return average
    except TypeError:
        print('В numbers записан некорректный тип данных')
        average = None
        return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
print(f'Результат 5: {calculate_average([])}')  # Всё должно работать
