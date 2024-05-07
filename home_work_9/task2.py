# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file.

code_to_write = '''
import json
import math
import random
import csv


def generate_csv_file(file_name: str, rows: int):
#     if rows < 100 or rows > 1000:
#         rows = random.randint(100, 1000)
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f, dialect='excel')
        for _ in range(rows):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            c = random.randint(1, 100)
            csv_writer.writerow((a, b, c))


def save_to_json(func):
    def wrapper(args):
        with open(args, 'r', encoding='utf-8', newline='') as f_read:
            csv_file = csv.reader(f_read, dialect='excel')
            all_data = []
            for line in csv_file:
                dict_result = dict()
                a, b, c = line
                result = func(int(a), int(b), int(c))
                dict_result['parameters'] = line
                dict_result['result'] = result
                all_data.append(dict_result)
        with open('results.json', 'w', encoding='utf-8') as f_write:
            json.dump(all_data, f_write)
        return all_data
    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))

    if dis_form > 0:
        x1 = (-b + sqrt_val) / (2 * a)
        x2 = (-b - sqrt_val) / (2 * a)
        return x1, x2

    elif dis_form == 0:
        return -b / (2 * a)

    else:
        return None
'''
with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
