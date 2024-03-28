# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def string_to_word_new_line(text_str):
    split_text = sorted(text_.split())
    max_len = max(map(lambda x: len(x), split_text))
    for i in enumerate(split_text, 1):
        print(f'{i[0]} {i[1]:>{max_len}}')


text_ = 'Привет, я Алеша! Познакомимся?'
string_to_word_new_line(text_)
