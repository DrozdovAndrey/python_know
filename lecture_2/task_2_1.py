a = 'edaeff'
print(type(a))
print(id(a))
print(hash(a))

data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

data = 3.14
print(isinstance(data, (int, float, complex)))

num = 2 + 2 * 2
digit = 36 // 6
print(num == digit)
print(num is digit)

a = 5
print(a, id(a))
a += 1
print(a, id(a))

#txt = 'Hello world!'
#txt[5] = '_'

txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))

a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c
print(a, id(a), b, id(b), c, id(c))

x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
# print(hash(my_list))

