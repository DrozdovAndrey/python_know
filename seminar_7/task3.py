# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def my_func():
    with (
        open('file_1.txt', 'r', encoding='utf-8') as f1,
        open('file_2.txt', 'r', encoding='utf-8') as f2,
        open('file_3.txt', 'w', encoding='utf-8') as f3
    ):
        list_f1 = []
        list_f2 = []
        for i in f1:
            a, b = i.split(',')
            a = int(a)
            b = float(b)
            list_f1.append(a * b)
        for i in f2:
            list_f2.append(i[:-1])
        max_len = max(len(list_f1), len(list_f2))
        if len(list_f2) > len(list_f1):
            for i in range(len(list_f2) - len(list_f1)):
                list_f1.append(list_f1[i])
        elif len(list_f2) < len(list_f1):
            for i in range(len(list_f1) - len(list_f2)):
                list_f2.append(list_f2[i])
        for i in range(max_len):
            f3.writelines(f'{list_f2[i]}:{str(list_f1[i])}\n')


my_func()
