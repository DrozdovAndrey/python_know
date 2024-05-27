"""
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import pytest
from task1 import validate_str_only_lat


def test_return_original_string():
    assert validate_str_only_lat('this string return without changes') == 'this string return without changes'


def test_return_low_reg():
    assert validate_str_only_lat('This String RetUrn witHout chanGeS') == 'this string return without changes'


def test_return_without_punk_mark():
    assert validate_str_only_lat('this. string, return! without? changes') == 'this string return without changes'


def test_return_only_latin():
    assert (validate_str_only_lat('thрорваis strinоажыg reываturn ываwithout changesыва') ==
            'this string return without changes')


def test_input_all_stuff_in_one():
    assert (validate_str_only_lat('tHрорваiS! stRinоажыg? r.eываTurn ыва,withOut Chan:gesыва') ==
            'this string return without changes')


if __name__ == '__main__':
    pytest.main()
