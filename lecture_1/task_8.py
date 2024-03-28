#Цикл итератор for in
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for item in data:
    print(item)

#Цикл по целым числам, он же арифметический цикл, функция range()
num = int(input('Введите число: '))
for i in range(0, num, 2):
    print(i)

animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for animal in animals:
    print(animal)

#Цикл с нумерацией элементов, функция enumerate()
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)
