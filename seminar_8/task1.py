# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


def my_func():
    with open('file_3.txt', 'r', encoding='utf-8') as f:
        my_dict = {}
        for line in f:
            a, b = line.split(':')
            my_dict[a] = b[:-1]
        print(my_dict)
    with open('new_file_3.json', 'w', encoding='utf-8') as f2:
        json.dump(my_dict, f2, ensure_ascii=False)


my_func()
