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
    if check_multiplicity(amount):
        global bank_account
        global count
        global operations
        bank_account += decimal.Decimal(amount)
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
        count += 1
        if count % COUNTER4PERCENTAGES == 0:
            percet_dep = PERCENT_DEPOSIT * bank_account
            bank_account = bank_account + percet_dep
            operations.append(f'Начислены проценты {percet_dep} у.е Итого {bank_account} у.е')
    else:
        print(f'Сумма должна быть кратной 50 у.е.')


def withdraw(amount):
    global bank_account
    global count
    global operations
    if check_multiplicity(amount):
        bank_account -= decimal.Decimal(amount)
        count += 1
        if amount * PERCENT_REMOVAL < MIN_REMOVAL:
            bank_account -= MIN_REMOVAL
        elif amount * PERCENT_REMOVAL > MAX_REMOVAL:
            bank_account -= MAX_REMOVAL
        else:
            bank_account -= amount * PERCENT_REMOVAL
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {MIN_REMOVAL} у.е.. '
                          f'Итого {bank_account} у.е.')
        if count % COUNTER4PERCENTAGES == 0:
            percet_dep = PERCENT_DEPOSIT * bank_account
            bank_account = bank_account + percet_dep
            operations.append(f'Начислены проценты {percet_dep} у.е Итого {bank_account} у.е')
    else:
        print(f'Сумма должна быть кратной 50 у.е.')


def exit():
    global bank_account
    global operations
    if bank_account > RICHNESS_SUM:
        rich_sum = bank_account * RICHNESS_PERCENT
        bank_account -= rich_sum
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {rich_sum} у.е. '
                          f'Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account}')


def check_multiplicity(amount):
    return amount % MULTIPLICITY == 0


deposit(1000000000000000)
# withdraw(200)
# withdraw(300)
# deposit(500)
withdraw(3000)
exit()

print(operations)