"""
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
from logger import logger as log


class NegativeValueError(Exception):
    pass


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        if width < 0:
            log.error(f'NegativeValueError: Ширина должна быть положительной, а не {width}')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')

        else:
            self._width = width
        if height is None:
            self._height = width
        else:
            if height < 0:
                log.error(f'NegativeValueError: Высота должна быть положительной, а не {height}')
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            else:
                self._height = height
        log.info(msg=f'Create Rectangle: with = {self._width}, height = {self._height}')

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        s = 2 * (self._width + self._height)
        log.info(msg=f'{self.__repr__()}, perimetr = {s}')
        return s

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        p = self._width * self._height
        log.info(msg=f'{self.__repr__()}, area = {p}')
        return p

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self._width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        r1 = Rectangle(width, height)
        log.info(msg=f'{self.__repr__()} + {other.__repr__()} = {r1.__repr__()}')
        return r1

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        r1 = Rectangle(width, height)
        log.info(msg=f'{self.__repr__()} - {other.__repr__()} = {r1.__repr__()}')
        return r1

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        var = self.area() < other.area()
        log.info(msg=f'{self.__repr__()} < {other.__repr__()} = {var}')
        return var

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        var = self.area() == other.area()
        log.info(msg=f'{self.__repr__()} == {other.__repr__()} = {var}')
        return var

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        var = self.area() <= other.area()
        log.info(msg=f'{self.__repr__()} <= {other.__repr__()} = {var}')
        return var

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self._width} и {self._height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self._width}, {self._height})"

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @height.setter
    def height(self, height):
        if height < 0:
            log.error(f'NegativeValueError: Высота должна быть положительной, а не {height}')
            raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        else:
            self._height = height
            log.info(msg=f'Changed height = {self._height}')

    @width.setter
    def width(self, width):
        if width < 0:
            log.error(f'NegativeValueError: Ширина должна быть положительной, а не {width}')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        else:
            self._width = width
            log.info(msg=f'Changed width = {self._width}')


# r2 = Rectangle(3,5)
# r3 = Rectangle(15, 200)
# r2.perimeter()
# r3.area()
# r4 = r2 + r3
# r5 = r2 - r3
# var_less = r5 < r4
# var_eq = r2 == r3
# var_less_eq = r2 <= r3
# r5.width = 5
# r5.height = 3
# var_eq2 = r5 == r2
# # r1 = Rectangle(1, -5)
# # r5.width = -5
# r5.height = -3

