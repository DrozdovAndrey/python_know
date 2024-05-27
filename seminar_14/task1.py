"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.

Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""


def validate_str_only_lat(value: str) -> str:
    """
    Функция принимает строку и удаляет из текста все символы кроме букв латиского алфавита и пробелов. Вовращается
    строка в нижне регистре
    :param value: str
    :return: str
    >>> validate_str_only_lat('this string return without changes')
    'this string return without changes'
    >>> validate_str_only_lat('This String RetUrn witHout chanGeS')
    'this string return without changes'
    >>> validate_str_only_lat('this. string, return! without? changes')
    'this string return without changes'
    >>> validate_str_only_lat('thрорваis strinоажыg reываturn ываwithout changesыва')
    'this string return without changes'
    >>> validate_str_only_lat('tHрорваiS! stRinоажыg? r.eываTurn ыва,withOut Chan:gesыва')
    'this string return without changes'
    """
    new_value = ''
    for i in value:
        if i.isascii() and not i.isdigit():
            if i == ' ' and new_value[-1] == ' ':
                continue
            if i.isalpha() or i == ' ':
                new_value += i

    return new_value.lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
