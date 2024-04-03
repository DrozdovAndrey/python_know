MONTH_31 = (1, 3, 5, 7, 8, 10, 12)
MONTH_30 = (4, 6, 9, 11)
MONTH_28 = 2
date_to_prove = '12.5.-2022'


def date_to_proved() -> bool:
    global date_to_prove
    day, month, year = map(int, date_to_prove.split('.'))

    def check_year(year_: str) -> bool:
        if year_ % 400 == 0 or year_ % 4 == 0 and year_ % 100 != 0:
            return True
        else:
            return False
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month in MONTH_31 and day > 31:
        return False
    if month in MONTH_30 and day > 30:
        return False
    if month == MONTH_28 and day > 28 and not check_year(year):
        return False
    if month == MONTH_28 and day > 29 and check_year(year):
        return False
    return True


print(date_to_proved())
