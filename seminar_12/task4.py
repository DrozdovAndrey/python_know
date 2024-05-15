"""
задача 4. Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.

задача 5. Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.

задача 6. Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Rectangle:
    # __slots__ = ('_length', '_width')
    length = Range(1)
    width = Range(1)

    def __init__(self, length, width=None):
        self._length = length
        self._width = width if width else length

    # @property
    # def length(self):
    #     return self._length
    #
    # @length.setter
    # def length(self, value):
    #     if value > 0:
    #         self._length = value
    #     else:
    #         raise ValueError(f'Новая длинна должна быть больше 0')
    #
    # @property
    # def width(self):
    #     return self._width
    #
    # @width.setter
    # def width(self, value):
    #     if value > 0:
    #         self._width = value
    #     else:
    #         raise ValueError(f'Новая ширина должна быть больше 0')

    def calc_square(self):
        return self._width * self._width

    def calc_perimeter(self):
        return self._width * 2 + self._length * 2

    def __add__(self, other):
        if isinstance(other, Rectangle):
            length = self._length + other._length
            width = self._width + other._width
            return Rectangle(length, width)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            length = abs(self._length - other._length)
            width = abs(self._width - other._width)
            return Rectangle(length, width)
        raise TypeError

    def __str__(self):
        return f'{self._length = }, {self._width = }'

    def __eq__(self, other):
        return self.calc_square() == other.calc_square()

    def __ne__(self, other):
        return self.calc_square() != other.calc_square()

    def __lt__(self, other):
        return self.calc_square() < other.calc_square()

    def __gt__(self, other):
        return self.calc_square() > other.calc_square()

    def __le__(self, other):
        return self.calc_square() >= other.calc_square()

    def __ge__(self, other):
        return self.calc_square() <= other.calc_square()


r1 = Rectangle(10, 15)
r2 = Rectangle(5)
print(r1)
print(r2)

r3 = r1 + r2
print(r3)

r4 = r1 - r3
print(r4)
r1.width = 100
r1.length = 200
print(r1)
r2.length = 0
print(r2)

print(r1 == r4)
print(r1 != r4)
print(r1 < r2)
print(r1 > r3)
print(r1 >= r3)
print(r1 <= r2)
# print(Rectangle.__dict__)
# print(Rectangle.__slots__)
# # print(r1.__dict__)
# print(r1.__slots__)
