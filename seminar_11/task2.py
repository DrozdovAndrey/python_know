# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# Задача 3. Добавьте к задачам 1 и 2 строки документации для классов.

# Задача 4. Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    """Class storages attribute instance"""
    lst_archive = []
    twin = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, string: str, num: int):
        """add twin instance's last attribute"""
        if self.twin is not None:
            self.lst_archive.append(self.twin)
        self.string = string
        self.num = num
        self.twin = (self.string, self.num)

    def __str__(self):
        return f'string = {self.string}, name = {self.num}'

    def __repr__(self):
        return f'Archive({self.string}, {self.num})'


arch1 = Archive('ffjjdsaa', 78)
arch2 = Archive('fxaaaaazxc', 9)
arch3 = Archive('[[[[[[[[[', 7)
arch4 = Archive('bvbnm,.', 90)
print(Archive.lst_archive)
print(arch1)
print(repr(arch2))
