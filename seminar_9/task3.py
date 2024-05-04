# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
from typing import Callable
import os
import json


def save_to_json(func: Callable):
    lst = []

    def wrapper(*args, **kwargs):
        name = func.__name__ + '.json'
        lst_args = args
        lst_kwargs = kwargs
        result = func(*args, **kwargs)
        my_dict = dict()
        if len(lst_args) != 0:
            my_dict['lst_args'] = lst_args
        for key, value in lst_kwargs.items():
            my_dict[key] = value
        my_dict['result'] = result
        # хз верно ли распаковал ключевые аргументы - ключевые аргументы распаковываются в словарь
        with open(name, 'w', encoding='utf-8') as fw:
            if len(lst) == 0:
                json.dump(my_dict, fw)
                lst.append(my_dict)
            else:
                lst.append(my_dict)
                json.dump(lst, fw)

        return result

    return wrapper


@save_to_json
def sum_num(num1=1, num2=1):
    return num1 + num2


sum_num(num2=3, num1=5)
sum_num(num2=3, num1=5)
sum_num(num2=3, num1=5)
sum_num(num2=3, num1=5)

