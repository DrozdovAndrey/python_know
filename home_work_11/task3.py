class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2

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
        return f'Прямоугольник со сторонами {self.length} и {self.width}'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))
