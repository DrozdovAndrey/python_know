names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

# Введите ваше решение ниже
# {name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)}
my_dict = {name: salaries * float(bonu[:-1]) / 100 for name, salaries, bonu in zip(names, salary, bonus)}
print(my_dict)