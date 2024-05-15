# Метод __str__ возвращает строковое представление объекта, включая текущие записи (text и number) и архивированные
# записи (archive_text и archive_number).
#
# Метод __repr__возвращает строковое представление объекта, которое можно использовать для создания нового объекта того
# же класса с теми же записями.
#
# Архивированные записи могут быть получены через атрибуты archive_text и archive_number.
#
# Метод __new__ - это статический метод, который создает новый экземпляр класса. Первым аргументом метод __new__
#
# получает ссылку на класс (cls), а затем может принимать дополнительные аргументы. Метод __new__ проверяет, существует
# ли уже экземпляр класса Archive (с использованием атрибута _instance). Если экземпляр существует, то метод вместо
# создания нового экземпляра добавляет текущие значения text и number в архив (списки archive_text и archive_number)
# для уже существующего экземпляра. Если экземпляр еще не существует, метод создает новый экземпляр класса Archive с
# пустыми архивами для текстовых и числовых записей. В любом случае метод возвращает созданный или существующий
# экземпляр класса Archive.
#
# Метод __init__ - это конструктор экземпляра класса, который вызывается после создания экземпляра с использованием
# метода __new__. Метод __init__ принимает два аргумента: text (строка) и number (целое число или число с плавающей
# точкой). В методе __init__устанавливаются атрибуты text и number текущего экземпляра класса для хранения переданных
# текстовой и числовой записей. Эти записи могут быть затем добавлены в архив (списки archive_text и archive_number)
# с использованием метода __new__.

class Archive:
    """Class storages attribute instance"""
    archive_text = []
    archive_number = []
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, string: str, num: int):
        """add twin instance's last attribute"""
        self.string = string
        self.num = num
        self.archive_text.append(self.string)
        self.archive_number.append(self.num)

    def __str__(self):
        return f"Text is {self.string} and number is {self.num}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Archive('{self.string}', {self.num})"




archive1 = Archive("First Text", 1)

print(archive1)

archive2 = Archive("Second Text", 2)

print(archive2)

archive3 = Archive("Third Text", 3)

print(archive3)