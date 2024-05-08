# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.
class Person:
    def __init__(self, name, surname, family_name, age):
        self.name = name
        self.surname = surname
        self.family_name = family_name
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.family_name} {self.name} {self.surname}'

    def get_age(self):
        return self._age


# p1 = Person('Andrey', 'Anatol', 'Drozdov', 36)
# print(p1.full_name())
# print(p1.get_age())
# p1.birthday()
# print(p1.get_age())