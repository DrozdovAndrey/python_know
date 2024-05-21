"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.

"""


def get_number():
    while True:
        num = input('Введите целое число или вещественное: ')
        if num.isdigit():
            num = int(num)
            break
        else:
            try:
                num = float(num)
                break
            except ValueError as e:
                print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                      f'Попробуйте снова')
    return num


print(get_number())

