def sum_a_b(a: float, b: float):
    print(a + b)


def sub_a_b(a: float, b: float):
    print(a - b)


def multi_a_b(a: float, b: float):
    print(a * b)


def dev_a_b(a: float, b: float):
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')


def mod_a_b(a: float, b: float):
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')


def pow_a_b(a: float, b: float):
    print(a ** b)


def div_a_b(a: float, b: float):
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')


a = float(input('ведите число a: '))
b = float(input('ведите число b: '))
input_operation = input('ведите операцию +, -, /, *, mod, pow, div: ')

match input_operation:
    case '+':
        sum_a_b(a, b)
    case '-':
        sub_a_b(a, b)
    case '*':
        multi_a_b(a, b)
    case '/':
        dev_a_b(a, b)
    case 'mod':
        mod_a_b(a, b)
    case 'pow':
        pow_a_b(a, b)
    case 'div':
        div_a_b(a, b)

# if input_operation == '+':
#         sum_a_b(a, b)
# elif input_operation == '-':
#         sub_a_b(a, b)
# elif input_operation == '*':
#         multi_a_b(a, b)
# elif input_operation == '/':
#         dev_a_b(a, b)
# elif input_operation == 'mod':
#         mod_a_b(a, b)
# elif input_operation == 'pow':
#         pow_a_b(a, b)
# elif input_operation == 'div':
#         div_a_b(a, b)
# else:
#     print('Я не понял что вы написали')
