import fractions


def parse_string_to_int(input_string):
    index_slash = input_string.find('/')
    numerator = int(input_string[:index_slash])
    denominator = int(input_string[index_slash + 1:])
    return numerator, denominator


def sum_fraction(numerator_1, denominator_1, numerator_2, denominator_2):
    sum_frac = str(numerator_1 * denominator_2 + numerator_2 * denominator_1) + '/' + str(denominator_1 * denominator_2)
    print(f'Сумма дробей: {sum_frac}')


def multy_fraction(numerator_1, denominator_1, numerator_2, denominator_2):
    multy_frac = str(numerator_1 * numerator_2) + '/' + str(denominator_1 * denominator_2)
    print(f'Произведение дробей: {multy_frac}')


frac1 = "1/2"
frac2 = "1/3"

numerat_1, denominat_1 = parse_string_to_int(frac1)
numerat_2, denominat_2 = parse_string_to_int(frac2)
sum_fraction(numerat_1, denominat_1, numerat_2, denominat_2)
multy_fraction(numerat_1, denominat_1, numerat_2, denominat_2)
print(f'Сумма дробей: {fractions.Fraction(frac1) + fractions.Fraction(frac2)}')
print(f'Произведение дробей: {fractions.Fraction(frac1) * fractions.Fraction(frac2)}')
