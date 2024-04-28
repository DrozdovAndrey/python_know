# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__.py и запишите в него все функции:
# get_dir_size,
# save_results_to_json,
# save_results_to_csv,
# save_results_to_pickle, traverse_directory.


code_to_write = '''
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
'''
with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)