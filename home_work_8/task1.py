# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит
# эту директорию и все вложенные директории. Результаты обхода должны быть сохранены в нескольких
# форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:
#
# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и
# директории в байтах. Важные детали:
#
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
#
# Для файлов сохраните их размер в байтах.
#
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
# и вложенных директорий.
#
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
#
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
#
# Для обхода файловой системы вы можете использовать модуль os.
#
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и
# возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных
# файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
#
# Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
# При этом сначала добавляются файлы, а затем директории.
#
# Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
# и затем получается размер файла (size = os.path.getsize(path)). Информация о файле добавляется в список results
# в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
#
# Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)),
# и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого. Информация о
# директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
# Введите ваше решение ниже
import csv
import json
import os
import pickle


def get_dir_size(path: str):
    size = 0
    for path_, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path_, f)
            size += os.path.getsize(fp)
    return size


def traverse_directory(directory: str):
    results = []
    for dir_path, dir_name, file_name in os.walk(directory):
        for file in file_name:
            path = os.path.join(dir_path, file)
            size = os.path.getsize(path)
            my_file_dict = dict()
            my_file_dict['Path'] = path
            my_file_dict['Type'] = 'File'
            my_file_dict['Size'] = size
            results.append(my_file_dict)
        for dir_ in dir_name:
            path_dir = os.path.join(dir_path, dir_)
            dir_size = get_dir_size(path_dir)
            my_dir_dict = dict()
            my_dir_dict['Path'] = path_dir
            my_dir_dict['Type'] = 'Directory'
            my_dir_dict['Size'] = dir_size
            results.append(my_dir_dict)
    return results


def save_results_to_json(results: list, name='results.json'):
    with open(name, 'w', encoding='utf-8') as file:
        json.dump(results, file)


def save_results_to_csv(results: list, name='results.csv'):
    with open(name, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames = ['Path', 'Type', 'Size'], dialect='excel')
        csv_writer.writeheader()
        csv_writer.writerows(results)


def save_results_to_pickle(results: list, name='results.pkl'):
    with open(name, 'wb') as file:
        pickle.dump(results, file)


lst = traverse_directory('C:\\Users\\drozd\\PycharmProjects\\pythonProject\\seminar_8')
save_results_to_json(lst)
save_results_to_csv(lst)
save_results_to_pickle(lst)
