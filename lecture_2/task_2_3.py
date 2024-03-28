# a: int | float = 42
# b: float = float(input('Введи число: '))
# a = a / b


def my_func(data: list[int | float]) -> float:
    res = sum(data) / len(data)
    return res


print(my_func([2, 5.5, 15, 8.0, 13.74]))

print("Hello world!".__doc__)
print(str.__doc__)

print("Hello world!".upper())
print("Hello world!".count('l'))

print(dir("Hello world!"))

print("Hello world!".lower())

help("Hello world!")

help(str)

help()