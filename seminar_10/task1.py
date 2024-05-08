# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
class Circle:
    PI = 3.14

    def __init__(self, rad):
        self.rad = rad

    def calculate_len_circle(self):
        return 2 * self.PI * self.rad

    def calculate_square_circle(self):
        return self.PI * (self.rad ** 2)


circle1 = Circle(10)
print(circle1.calculate_len_circle(), circle1.calculate_square_circle())
