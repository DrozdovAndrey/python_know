# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import os
import pickle


def my_func():
    lst = os.listdir('C:\\Users\\drozd\\PycharmProjects\\pythonProject\\seminar_8')
    lst_json = []
    for i in lst:
        if i.endswith('.json'):
            lst_json.append(i)
    for path in lst_json:
        with open(path, 'r', encoding='utf-8') as file_read:
            data = json.load(file_read)
        new_path = os.path.splitext(path)[0] + '.pickle'
        with open(new_path, 'wb') as file_write:
            pickle.dump(data, file_write)


my_func()
