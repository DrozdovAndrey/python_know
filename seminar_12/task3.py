"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class GenFac:
    def __init__(self, num, start=1, step=1):
        self.num = num
        self.start = start
        self.step = step
        self.factorial = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.num:
            self.factorial = self.factorial * (self.start + self.step)
            self.start += self.step
            return self.factorial
        raise StopIteration


a = GenFac(10, 2, 2)
for i in a:
    print(i)
