# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
from random import randint as rint, uniform as rfloat


def my_func(cout_lines, name_file):
    with open(name_file, 'w', encoding='utf-8') as f:
        for i in range(cout_lines):
            f.writelines(f'{rint(-1000, 1000)},{rfloat(-1000, 1000)}\n')


my_func(15, 'file_1.txt')
