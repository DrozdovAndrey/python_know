# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def show_skill(self):
        return f'{self.name} {self.spec}'


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


dog1 = Dog('reks', 1, 'runnig so fast')
cat1 = Cat('vas', '2', 'sleep so long')
fish1 = Fish('riba', 3, 'just swim')
animal1 = Animal('who i am', '33')
for i in [animal1, dog1, cat1, fish1]:
    print(i.show_skill())
