# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable


def my_func(count: int) -> Callable:
    def guess_number(guess_num: int):
        nonlocal count
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

    return guess_number


guess = my_func(10)
guess(60)
