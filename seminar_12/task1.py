"""
Задача 1. Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
Задача 2. Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.

"""
import json


class MyFunc:

    def __init__(self, max_count):
        self.max_count = max_count
        self.storage_value = list()
        self.storage_result = list()

    def __call__(self, value):
        factorial = value
        for i in range(1, value):
            factorial = factorial * i
        if len(self.storage_value) >= self.max_count:
            self.storage_value.pop(0)
            self.storage_result.pop(0)
        self.storage_result.append(factorial)
        self.storage_value.append(value)
        return factorial

    def __str__(self):
        return '\n'.join([f'fac {self.storage_value[i]} = {self.storage_result[i]}'
                          for i in range(len(self.storage_value))])

    def __enter__(self):
        self.my_dict = {}
        for i in range(len(self.storage_value)):
            self.my_dict[self.storage_value[i]] = self.storage_result[i]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('my_dict.json', 'w', encoding='utf-8') as f:
            json.dump(self.my_dict, f)


a = MyFunc(7)
print(a(3))
print(a)
print(a(4))
print(a)
print(a(5))
print(a)
print(a(6))
print(a)
print(a(5))
print(a)
print(a(6))
print(a)
print(a(5))
print(a)
print(a(6))
print(a)
print(a(4))
print(a)
print(a(5))
print(a)
with a as y:
    print(a)
