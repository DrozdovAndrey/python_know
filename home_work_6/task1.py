#date_to_prove = 15.4.2023

# Введите ваше решение ниже
MONTH_31 = (1, 3, 5, 7, 8, 10, 12)
MONTH_30 = (4,

def date_to_prove(str_: str) -> bool:
    day, month, year = str_.split('.')
    if month < 1 or month > 12:
        return False
    if month
    if day < 1 or day > 31