"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import unittest
from task1 import validate_str_only_lat


class TestTask1(unittest.TestCase):
    def test_return_original_string(self):
        self.assertEqual(validate_str_only_lat('this string return without changes'),
                         'this string return without changes')

    def test_return_low_reg(self):
        self.assertEqual(validate_str_only_lat('This String RetUrn witHout chanGeS'),
                         'this string return without changes')

    def test_return_without_punk_mark(self):
        self.assertEqual(validate_str_only_lat('this. string, return! without? changes'),
                         'this string return without changes')

    def test_return_only_latin(self):
        self.assertEqual(validate_str_only_lat('thрорваis strinоажыg reываturn ываwithout changesыва'),
                         'this string return without changes')

    def test_input_all_stuff_in_one(self):
        self.assertEqual(validate_str_only_lat('tHрорваiS! stRinоажыg? r.eываTurn ыва,withOut Chan:gesыва'),
                         'this string return without changes')


if __name__ == '__main__':
    unittest.main()
