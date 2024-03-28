# num = 2
#

def is_simple(input_number: int):
    k = 0
    for i in range(2, input_number // 2 + 1):
        if input_number % i == 0:
            k = k + 1
    if k <= 0:
        print("Число простое")
    else:
        print("Число не является простым")


num = int(input('Input int: '))
if 1 < num < 100000:
    is_simple(num)
else:
    print('Число должно быть больше 1 и меньше 100000')
