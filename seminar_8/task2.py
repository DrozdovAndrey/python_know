# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import os
import json

MIN_ACCESS_LEVEL = 1
MAX_ACCESS_LEVEL = 7
PATH_DB = 'user_db.json'


def load_json() -> dict:
    if os.path.exists(PATH_DB):
        with open(PATH_DB, 'r', encoding='utf_8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def upload_json(user_db: dict):
    with open(PATH_DB, 'w', encoding="utf-8") as file:
        json.dump(user_db, file, ensure_ascii=False)


def input_name() -> str:
    """Функция запрашивает и возвращает имя"""

    return input('Введите ваше имя: ')


def input_id(set_ids: set) -> str:
    """Функция запрашивает и возвращает id еще нужна проверка на уникальрость айди"""
    while True:
        id_ = input('Введите id: ')
        if id_.isdigit():
            if id_ not in set_ids:
                return id_


def create_set_ids(user_db: dict) -> set:
    set_ids = set()
    for list_ids in user_db.values():
        for dict_ids in list_ids:
            for id_ in dict_ids.keys():
                set_ids.add(id_)
    return set_ids


def input_access_level() -> str:
    """Функция запрашивает, валидирует и возвращает уровень доступа"""
    while True:
        access_level = input('Введите уровень доступа')
        if access_level.isdigit():
            if MIN_ACCESS_LEVEL <= int(access_level) <= MAX_ACCESS_LEVEL:
                return access_level


def main():
    while True:
        user_db = load_json()
        name = input_name()
        if not name:
            break
        id_name = input_id(create_set_ids(user_db))
        access_level = input_access_level()
        if access_level not in user_db.keys():
            user_db[access_level] = [{id_name: name}]
        else:
            user_db[access_level].append({id_name: name})
        upload_json(user_db)


main()

# my_dict = {'1': [{'1': 'Andrey'}, {'2': 'LEx'}]}
# print(my_dict)
# my_dict['1'].append({'3': 'gobl'})
#
# print(my_dict)