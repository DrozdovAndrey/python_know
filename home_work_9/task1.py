# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой
# строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
#
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
#
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
#
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
#
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
#
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты
# вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация
# о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
import json
import math
import random
import csv


def generate_csv_file(file_name: str, rows: int):
    # if rows < 100 or rows > 1000:
    #     rows = random.randint(100, 1000)
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f, dialect='excel')
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)


def save_to_json(func):
    def wrapper(args):
        with open(args, 'r', encoding='utf-8', newline='') as f_read:
            csv_file = csv.reader(f_read, dialect='excel')
            all_data = []
            for line in csv_file:
                a, b, c = map(int, line)
                result = func(a, b, c)
                dict_result = {'parameters': [a, b, c], 'result': result}
                all_data.append(dict_result)
        with open('results.json', 'w', encoding='utf-8') as f_write:
            json.dump(all_data, f_write)
        return all_data
    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    dis_form = b**2 - 4 * a * c

    if dis_form > 0:
        x1 = (-b + dis_form**0.5) / (2 * a)
        x2 = (-b - dis_form**0.5) / (2 * a)
        return x1, x2

    elif dis_form == 0:
        return -b / (2 * a)

    else:
        return None


# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")
# with open('input_data.csv', 'r', encoding='utf-8', newline='') as f_read:
#     csv_reader = csv.reader(f_read, dialect='excel')
#     all_data = []
#     for line in csv_reader:
#         dict_result = dict()
#         a, b, c = line
#         result = find_roots(int(a), int(b), int(c))
#         dict_result['parameters'] = line
#         dict_result['result'] = result
#         all_data.append(dict_result)
#     print(all_data)

generate_csv_file("input_data.csv", 1500)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==1500)
