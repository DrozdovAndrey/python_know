# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def add_numbers_to_dict(text_str):
    text_str = text_str.split()
    my_dict = {chr(int(text_str[0])): ord(text_str[1])}
    print(my_dict)

    
text = '22 1'
add_numbers_to_dict(text)
