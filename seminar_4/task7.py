# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def my_func(dict_: dict):
    my_dict = {}
    for i, j in dict_.items():
        if sum(j) < 0:
            my_dict[i] = False
        else:
            my_dict[i] = True
    return all(my_dict.values())


my_dict1 = {'aic': [10, 11, -12, -5], 'cofe': [10, 11, -6, -5], 'latte': [-10, 30, -12, -5]}
print(my_func(my_dict1))
