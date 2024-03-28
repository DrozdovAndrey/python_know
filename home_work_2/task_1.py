num = 324235
num_2 = num
HEX_BASE = 16
HEX_10 = (10, 'A')
HEX_11 = (11, 'B')
HEX_12 = (12, 'C')
HEX_13 = (13, 'D')
HEX_14 = (14, 'E')
HEX_15 = (15, 'F')

hex_num = ''

while num:
    ost = num % HEX_BASE
    if ost in HEX_10:
        ost = HEX_10[1]
    elif ost in HEX_11:
        ost = HEX_11[1]
    elif ost in HEX_12:
        ost = HEX_12[1]
    elif ost in HEX_13:
        ost = HEX_13[1]
    elif ost in HEX_14:
        ost = HEX_14[1]
    elif ost in HEX_15:
        ost = HEX_15[1]

    hex_num = str(ost) + hex_num
    num = num // HEX_BASE

print(f'Шестнадцатеричное представление числа: {hex_num}')
print(f'Проверка результата: {hex(num_2)}')
