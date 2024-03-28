import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

# Введите ваше решение ниже
def deposit(amount):
    globals()['bank_account'] += decimal.Decimal(amount)


def withdraw(amount):
    globals()['bank_account'] -= decimal.Decimal(amount)


def exit():
    pass


def check_multiplicity(amount):
    pass


deposit(1000)
withdraw(200)
#exit()

#print(operations)
print(bank_account)