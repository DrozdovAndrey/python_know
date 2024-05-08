# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from task3 import Person


class Employer(Person):
    def __init__(self, name, surname, family_name, age, id_p):
        super().__init__(name, surname, family_name, age)
        self.id_p = id_p
        self.level = sum(list(map(int, id_p))) % 7


coach = Employer('dro', 'dgkjgkd', 'dgfdhd', 20, '25472539')
print(coach.id_p, coach.level)
