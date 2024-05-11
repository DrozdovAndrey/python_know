# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задача 6. Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def calc_square(self):
        return self.width * self.width

    def calc_perimeter(self):
        return self.width * 2 + self.length * 2

    def __add__(self, other):
        if isinstance(other, Rectangle):
            length = self.length + other.length
            width = self.width + other.width
            return Rectangle(length, width)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            length = abs(self.length - other.length)
            width = abs(self.width - other.width)
            return Rectangle(length, width)
        raise TypeError

    def __str__(self):
        return f'{self.length = }, {self.width = }'

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

print(r1 == r4)
print(r1 != r4)
print(r1 < r2)
print(r1 > r3)
print(r1 >= r3)
print(r1 <= r2)