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
        # global count
        global operations
        bank_account += decimal.Decimal(amount)
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
        # count += 1
        # if count % COUNTER4PERCENTAGES == 0:
        #     percet_dep = PERCENT_DEPOSIT * bank_account
        #     bank_account = bank_account + percet_dep
        #     operations.append(f'Начислены проценты {percet_dep} у.е Итого {bank_account} у.е')


def withdraw(amount):
    global bank_account
    # global count
    global operations
    # count += 1
    if amount * PERCENT_REMOVAL < MIN_REMOVAL:
        if check_multiplicity(amount) and bank_account - amount - MIN_REMOVAL >= 0:
            bank_account -= MIN_REMOVAL + amount
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {MIN_REMOVAL} у.е.. '
                              f'Итого {bank_account} у.е.')
        else:
            operations.append(f'Недостаточно средств. Сумма с комиссией {amount + MIN_REMOVAL} у.е. '
                              f'На карте {bank_account} у.е.')
    elif amount * PERCENT_REMOVAL > MAX_REMOVAL:
        if check_multiplicity(amount) and bank_account - amount - MAX_REMOVAL >= 0:
            bank_account -= MAX_REMOVAL + amount
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {MAX_REMOVAL} у.е.. '
                              f'Итого {bank_account} у.е.')
        else:
            operations.append(f'Недостаточно средств. Сумма с комиссией {amount + MAX_REMOVAL} у.е. '
                              f'На карте {bank_account} у.е.')
    else:
        if check_multiplicity(amount) and bank_account - amount - amount * PERCENT_REMOVAL >= 0:
            bank_account -= amount * PERCENT_REMOVAL + amount
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {amount * PERCENT_REMOVAL} у.е.. '
                              f'Итого {bank_account} у.е.')
        else:
            operations.append(f'Недостаточно средств. Сумма с комиссией {amount + MAX_REMOVAL} у.е. '
                              f'На карте {bank_account} у.е.')
    # if count % COUNTER4PERCENTAGES == 0:
    #     percet_dep = PERCENT_DEPOSIT * bank_account
    #     bank_account = bank_account + percet_dep
    #     operations.append(f'Начислены проценты {percet_dep} у.е Итого {bank_account} у.е')


def exit():
    global bank_account
    global operations
    if bank_account > RICHNESS_SUM:
        rich_sum = bank_account * RICHNESS_PERCENT
        bank_account -= rich_sum
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {rich_sum} у.е. '
                          f'Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


def check_multiplicity(amount):
    if amount % MULTIPLICITY != 0:
        print(f'Сумма должна быть кратной 50 у.е.')
    return amount % MULTIPLICITY == 0


deposit(173)
withdraw(21)
exit()

print(operations)

# решение в задаче
# import decimal
#
# MULTIPLICITY = 50
# PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
# MIN_REMOVAL = decimal.Decimal(30)
# MAX_REMOVAL = decimal.Decimal(600)
# PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
# COUNTER4PERCENTAGES = 3
# RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
# RICHNESS_SUM = decimal.Decimal(10_000_000)
#
# bank_account = decimal.Decimal(0)
# count = 0
# operations = []
#
# def check_multiplicity(amount):
#     """Проверка кратности суммы"""
#     if (amount % MULTIPLICITY) != 0:
#         print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
#         return False
#     return True
#
# def deposit(amount):
#     """Пополнение счета"""
#     global bank_account, count
#     if not check_multiplicity(amount):
#         print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
#         return False  # Операция не выполнена из-за некратной суммы
#     count += 1
#     bank_account += amount
#     operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
#     return True
#
#
# def withdraw(amount):
#     """Снятие денег"""
#     global bank_account, count
#     percent = amount * PERCENT_REMOVAL
#     percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
#     if bank_account >= amount + percent:
#         count += 1
#         bank_account = bank_account - amount - percent
#         operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е..
#         Итого {int(bank_account)} у.е.')
#     else:
#         operations.append(
#             f'Недостаточно средств. Сумма с комиссией {amount + int(percent)} у.е. На карте {int(bank_account)} у.е.')
#
# def exit():
#     global bank_account, operations
#     if bank_account > RICHNESS_SUM:
#         percent = bank_account * RICHNESS_PERCENT
#         bank_account -= percent
#         operations.append(
#             f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е.')
#     operations.append(f'Возьмите карту на которой {bank_account} у.е.')
#
#
