# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.
input_string = 'fefhk efihaliehfha liaehlfhl qlehflhaf'


def string_to_dict(input_str: str) -> dict:
    return {i: ord(i) for i in input_str}


iterator_dict = iter(string_to_dict(input_string).items())
for key in range(5):
    print(next(iterator_dict))
