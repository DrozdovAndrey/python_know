a = 1
b = 4
c = 3


if a < (b + c) and b < (a + c) and c < (a + b):
    print('Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')