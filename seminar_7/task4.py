# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from random import randint as rint, randbytes
RANGE_START = 97
RANGE_STOP = 122


def my_func(expansion_str, min_name=6, max_name=30, min_bite=256, max_bite=4096, count_files=42):
    for i in range(count_files):
        with open(f'{gen_name(min_name, max_name)}{i+1}.{expansion_str}', 'wb') as f:
            f.write(randbytes(rint(min_bite, max_bite)))


def gen_name(min_name, max_name):
    count_letters = rint(min_name, max_name)
    name = ''
    for _ in range(count_letters):
        name += chr(rint(RANGE_START, RANGE_STOP))
    return name


my_func('txt', 6, 10, 26, 40,3)