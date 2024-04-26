# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import pickle
import csv


def my_func():
    with open('new_user_db.pickle', 'rb') as file_read:
        data = pickle.load(file_read)
        print(data)
    with open('new_file.csv', 'w', newline='', encoding='utf-8') as file_write:
        csv_write = csv.DictWriter(file_write, fieldnames=["id", "name", "access_level"], dialect='excel')
        csv_write.writeheader()
        for dict_ in data:
            csv_write.writerow(dict_)


my_func()
