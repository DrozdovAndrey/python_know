"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
import unittest
from seminar_12 import task4


class TestRect(unittest.TestCase):

    def setUp(self):
        self.rect1 = task4.Rectangle(5, 10)
        self.rect2 = task4.Rectangle(10, 5)
        self.rect3 = task4.Rectangle(3, 10)

    def test_is_instance(self):
        self.assertRaises(TypeError, task4.Rectangle, 3.14, 3.13)

    def test_rect_square(self):
        self.assertEqual(self.rect1.calc_square(), 50)

    def test_rect_perimetr(self):
        self.assertEqual(self.rect2.calc_perimeter(), 30)

    def test_rect_equals(self):
        self.assertEqual(self.rect1, self.rect2)

    def test_rect_not_equal(self):
        self.assertNotEqual(self.rect2, self.rect3)

    def test_greater_rect(self):
        self.assertGreater(self.rect1, self.rect3)

    def test_greater_equal_rect(self):
        self.assertGreaterEqual(self.rect1, self.rect2)


if __name__ == '__main__':
    unittest.main()
