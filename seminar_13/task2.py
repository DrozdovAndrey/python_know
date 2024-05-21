"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_value_from_dict(my_dict: dict, key, value):
    try:
        return my_dict[key]
    except KeyError:
        return value


my_dict = {'1': 1, '2': 2, '3': 3}
print(get_value_from_dict(my_dict, 1, 100))

