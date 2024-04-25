# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json


def read_csv(csv_name: str, json_name: str):
    with open(csv_name, 'r', newline='') as fr:
        csv_file = csv.reader(fr)
        count = 0
        keys = []
        lst = []
        for line in csv_file:
            if count == 0:
                for key in line:
                    keys.append(key)
                count += 1
            else:
                len_lst = len(keys)
                my_dict = dict()
                for i in range(len_lst):
                    my_dict[keys[i]] = line[i]
                lst.append(my_dict)
    with open(json_name, 'w', encoding='utf-8') as fw:
        json.dump(lst, fw)


read_csv('user_db.csv', 'new_user_db.json')
