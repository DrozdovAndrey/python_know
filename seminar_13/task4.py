"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
import json


class Users:
    def __init__(self, name, personal_id, access_level):
        self.name = name
        self.personal_id = personal_id
        self.access_level = access_level

    def __repr__(self):
        return f'Users("{self.name}", "{self.personal_id}", "{self.access_level}")'


def create_users_from_bd(file_name):
    lst = []
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
            for i in my_dict:
                personal_id = i['id']
                name = i['name']
                access_level = i['access_level']
                lst.append(Users(name, personal_id, access_level))
    except FileNotFoundError as e:
        print(e)
    except json.decoder.JSONDecodeError as e:
        print('в файле нет ничего или херня')
    return lst


print(create_users_from_bd('new_user_db.json'))

