# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
from time import time


class MyString(str):
    """Docs for my class, extended from string"""
    def __new__(cls, value, name):
        """Method for additional atribute"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = time()
        return instance


line1 = MyString('привет это тестовая строка', 'андрей')
print(line1, line1.date, line1.name)
print(type(line1))


class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance
print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
print('Создаём второй раз')
b = NamedInt(73, 'Лучшее просто число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')
