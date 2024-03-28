import math
import decimal
import fractions

print(math.cos(30))

print(decimal.Decimal(math.pi))

decimal.getcontext().prec = 120
print(decimal.Decimal(math.pi**2))

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(type(f2))
print(f1 + f2)

a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')

print(divmod(42, 5))

print(round(0.363668638636386386, 4))

print(round(1.74937493))

print(abs(-48))
