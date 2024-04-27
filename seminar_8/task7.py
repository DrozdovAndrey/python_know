# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle

with open('new_file.csv', 'r', newline='') as file_read:
    csv_file = csv.reader(file_read, dialect='excel')
    lst_pickle = []
    for line in csv_file:
        lst_pickle.append(line)
    res = pickle.dumps(lst_pickle, protocol=pickle.DEFAULT_PROTOCOL)

print(res)
