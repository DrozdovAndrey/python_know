#
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
from task2 import load_json


def upload_to_csv():
    user_db = load_json()
    with open('user_db.csv', 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.DictWriter(f, fieldnames=["id", "name", "access_level"], dialect='excel',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        all_data = dict()
        for access_level, list_of_dict in user_db.items():
            for i in list_of_dict:
                for id_, name in i.items():
                    all_data['id'] = id_
                    all_data['name'] = name
                    all_data['access_level'] = access_level
                    csv_write.writerow(all_data)


upload_to_csv()
