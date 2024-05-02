# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
import random
from typing import Callable


def my_func(func: Callable) -> Callable:
    def wrapper(*args):
        a, b, *_ = args
        if a not in [x for x in range(1, 101)]:
            a = random.randint(1, 100)
        if b not in [y for y in range(1, 11)]:
            b = random.randint(1, 10)
        func(a, b)

    return wrapper


@my_func
def guess_number(guess_num: int, count: int = 1):
    while count:
        num = int(input('Input number: '))
        if num == guess_num:
            print('You win')
            break
        elif num > guess_num:
            print('Введите число меньше')
        else:
            print('Введите число больше')
        count -= 1
        if count == 0:
            print('вы проиграли')


guess_number(55, 23)
