# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def unicode_text(text_lst):
    for i in sorted(text_lst, reverse=True):
        i = ord(i)
        print(i)


text = list('fsjhfks ekhflkheflkh wekhflhkl, wehlfhwh! eidhwhi wewhihdwoh ?')
unicode_text(text)
