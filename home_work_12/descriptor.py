class Descriptor:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        for i in value.split():
            if not i.isalpha() or not i.istitle():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
