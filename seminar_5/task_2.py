#  Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.
input_string = 'fefhk efihaliehfha liaehlfhl qlehflhaf'


def string_to_dict(input_str: str) -> dict:
    return {i: ord(i) for i in input_str}


print(string_to_dict(input_string))
