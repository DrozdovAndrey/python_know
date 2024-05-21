"""
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class BaseExcept(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} значение нам не подходит'


class LevelError(BaseExcept):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value} уровня не существует'


class AccessError(BaseExcept):
    def __init__(self, name,  value):
        self.name = name
        super().__init__(value)

    def __str__(self):
        return f'{self.name}  не имеет доступ к уровню {self.value}'



# raise AccessError('ivan', 5)
raise LevelError(8)