# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.
c = (f'\n' if j == 11 else f' {j}*{i}={i * j:2d} ' for i in range(2,10) for j in range(2,12))
print(*c)
