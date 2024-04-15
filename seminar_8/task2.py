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
    if not os.path.exists(PATH_DB):
        with open(PATH_DB, 'w', encoding="utf-8") as file:
            json.dump(user_db)
    else:
        with open(PATH_DB, 'a', encoding="utf-8") as file:
            json.dump(user_db)



def input_name() -> str:
    """Функция запрашивает и возвращает имя"""

    return input('Введите ваше имя: ')


def input_id(set_ids: set) -> str:
    """Функция запрашивает и возвращает id еще нужна проверка на уникальрость айди"""
    while True:
        id_ = input('Введите id: ')
        if id_.isdigit():
            if int(id_) not in set_ids:
                return id_


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
        id_name = input_id(user_db)
        access_level = input_access_level()
