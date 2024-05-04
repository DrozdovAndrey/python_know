# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
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

