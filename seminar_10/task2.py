# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def calc_square(self):
        return self.width * self.width

    def calc_perimeter(self):
        return self.width * 2 + self.length * 2


r1 = Rectangle(10, 15)
r2 = Rectangle(5)
print(r1.calc_square(), r1.calc_perimeter())
print(r2.calc_square(), r2.calc_perimeter())