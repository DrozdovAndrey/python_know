# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
import json
import random
from typing import Callable


def counting_func(count: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(count):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return deco


def my_func(func: Callable) -> Callable:
    def wrapper(*args):
        a, b, *_ = args
        if a not in [x for x in range(1, 101)]:
            a = random.randint(1, 100)
        if b not in [y for y in range(1, 11)]:
            b = random.randint(1, 10)
        func(a, b)

    return wrapper


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
        # хз верно ли распаковал ключевые аргументы,
        with open(name, 'w', encoding='utf-8') as fw:
            if len(lst) == 0:
                json.dump(my_dict, fw)
                lst.append(my_dict)
            else:
                lst.append(my_dict)
                json.dump(lst, fw)

        return result

    return wrapper


@counting_func(3)
@my_func
@save_to_json
def guess_number(guess_num: int, count: int = 1):
    while count:
        num = int(input('Input number: '))
        if num == guess_num:
            print('You win')
            return 'you win'
        elif num > guess_num:
            print('Введите число меньше')
        else:
            print('Введите число больше')
        count -= 1
        if count == 0:
            print('вы проиграли')
            return 'you lose'


guess_number(55, 3)