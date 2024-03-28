import sys

x = int("42")
y = int(3.1415)
z = int("hello", base=30)
print(x, y, z, sep='\n')

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP

print(sys.getsizeof(10 ** 100))

# num = 7_901_123_456_789

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)

