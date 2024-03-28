# Списки, list
import copy

list_1 = list()
list_2 = list((3.14, True, "Hello world!"))
list_3 = []
list_4 = [3.14, True, "Hello world!"]
print('__________________________')

my_list = [2, 4, 6, 8, 10, 12]
print(my_list[0])
# print(my_list[6]) # IndexError: list index out of range
print('__________________________')

my_list = [2, 4, 6, 8, 10, 12]
print(my_list[-1])
# print(my_list[-10]) # IndexError: list index out of range
print('__________________________')

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b)
print(my_list)
my_list.append(c)
print(my_list)
print('__________________________')

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
# my_list.extend(a) # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)
my_list.extend(my_list)
print(my_list)
print('__________________________')

my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
# err = my_list.pop(10) # IndexError: pop index out of range
print('__________________________')

my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.count(2)
print(spam)
eggs = my_list.count(3)
print(eggs)
print('__________________________')

my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
eggs = my_list.index(4, spam + 1, 90)
print(eggs)
# err = my_list.index(3) # ValueError: 3 is not in list
print('__________________________')

my_list = [2, 4, 6, 8, 10, 12]
my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
my_list.insert(42, 73) # my_list.append(73)
print(my_list)
print('__________________________')

my_list = [2, 4, 6, 8, 10, 12, 6]
my_list.remove(6)
print(my_list)
# my_list.remove(3) # ValueError: list.remove(x): x not in list
print(my_list)
print('__________________________')

my_list = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]
# my_list.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
# res = sorted(my_list) # TypeError: '<' not supported between instances of 'int' and 'str'
print('__________________________')

my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')
print('__________________________')

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print('__________________________')

my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)
print('__________________________')

for item in reversed(my_list):
    print(item)
print('__________________________')

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)
print('__________________________')

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[::-1]
print(my_list, new_list, sep='\n')
print('__________________________')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:])
print(my_list[8:3:-1])
print(my_list[3::])
print(my_list[:7:])
print('__________________________')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')
print('__________________________')


my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')
print('__________________________')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
print('__________________________')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
print('__________________________')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(len(my_list))
print(len(matrix))
print(len(matrix[1]))
print('__________________________')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:6:2])
print(my_list.pop())
print(my_list.extend([314, 42]))
print(my_list.sort(reverse=False))
print(my_list)
print('__________________________')
