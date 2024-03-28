import decimal
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
backpack = dict()


for key, value in items.items():
    if max_weight - value >= 0:
        backpack[key] = value
        max_weight -= value
print(backpack)

