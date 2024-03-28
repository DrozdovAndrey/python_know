# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def my_func(lst, a, b):
    if 0 <= a < len(lst) and 0 <= b < len(lst):
        if a <= b:
            return sum(lst[a:b])
        else:
            return sum(lst[b:a])
    else:
        return sum(lst)


lst1 = [1, 2, 4, 2, 3, 4, 2, 6, 7]
a = 0
b = 12
print(my_func(lst1, a, b))
