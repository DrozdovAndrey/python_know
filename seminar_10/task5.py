# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Dog:
    def __init__(self, name, age, run):
        self.name = name
        self.age = age
        self.run = run

    def show_skill(self):
        return f'{self.name} {self.run} |'


class Cat:
    def __init__(self, name, age, sleep):
        self.name = name
        self.age = age
        self.sleep = sleep

    def show_skill(self):
        return f'{self.name} {self.sleep} |'


class Fish:
    def __init__(self, name, age, swim):
        self.name = name
        self.age = age
        self.swim = swim

    def show_skill(self):
        return f'{self.name} {self.swim} |'


dog1 = Dog('reks', 1, 'runnig so fast')
cat1 = Cat('vas', '2', 'sleep so long')
fish1 = Fish('riba', 3, 'just swim')
print(dog1.show_skill(), cat1.show_skill(), fish1.show_skill())
