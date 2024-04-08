# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
# 1040 - 1103
from random import randint as rint
A_LETTERS = 'аАеЕоОуУэЭюЮяЯ'
RANGE_START = 1072
RANGE_STOP = 1103


def my_func(count_names):

    names = []
    for i in range(count_names):
        count_letters = rint(4, 7)
        flag = False
        while not flag:
            name = ''
            for _ in range(count_letters):
                name += chr(rint(RANGE_START, RANGE_STOP))
            if is_a_letter(name):
                names.append(name.capitalize())
                flag = True
    return names


def is_a_letter(name_str):
    list_name = list(name_str)
    for i in list_name:
        if i in A_LETTERS:
            return True
    return False


print(my_func(5))
