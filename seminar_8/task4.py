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


def read_csv(csv_name: str, json_name:str):
    with open (csv_name, 'r', newline='') as fr:
        csv_file = csv.reader(fr)
        keys = []
        count = 0
        my_dict = dict()
        for line in csv_file:
            if count == 0:
                keys = line
                count += 1
            else:
                my_dict


with open('data_in_csv.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
        print(type(line))


