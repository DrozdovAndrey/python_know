import csv
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


class Student:
    name = Descriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = dict()
        self.load_subjects(subjects_file)

    # дандер метод по получению значения из словоря с предметами - дескриптор
    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    # дандер метод, но по задаче он дескриптор по установке значения в ФИО
    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f, dialect='excel')
            for line in csv_file:
                for i in line:
                    self.subjects[i] = {'grade': [], 'test': []}

    def __str__(self):
        str_pr = ', '.join([i for i, j in self.subjects.items() if len(j['grade']) != 0 or len(j['test']) != 0])
        return f'Студент: {self.name}\nПредметы: {str_pr}'

    def add_grade(self, subject, grade):
        count = 0
        if isinstance(grade, int) and grade in range(2, 6):
            for item, value in self.subjects.items():
                if item == subject:
                    value['grade'].append(grade)
                    count += 1
        else:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        if count == 0:
            raise ValueError(f'Предмет {subject} не найден')

    def add_test_score(self, subject, test_score):
        if isinstance(test_score, int) and test_score in range(0, 101):
            for item, value in self.subjects.items():
                if item == subject:
                    value['test'].append(test_score)
        else:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')

    def get_average_test_score(self, subject):
        count = 0
        for item, value in self.subjects.items():
            if item == subject:
                count += 1
                return sum(value['test']) / len(value['test'])
        if count == 0:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self):
        sum_all = 0
        count = 0
        for value in self.subjects.values():
            if len(value['grade']) != 0:
                sum_all += sum(value['grade'])
                count += len(value['grade'])
        return sum_all / count

# sub = dict()
# with open('subjects.csv', 'r', newline='', encoding='utf-8') as f:
#     csv_file = csv.reader(f, dialect='excel')
#     for line in csv_file:
#         for i in line:
#             sub[i] = {'grade': [], 'test': []}

# print(sub)
#
# for item, value in sub.items():
#     if item == 'Физика':
#         value['grade'] = [1, 2]
#         value['test'] = [3, 4]
#     if item == 'Математика':
#         value['grade'] = [5, 6]
#         value['test'] = [1, 7]
#
# print(sub)
# lst_str = []
# for i, j in sub.items():
#     if len(j['grade']) != 0 or len(j['test']) != 0:
#         lst_str.append(i)
#
# str_pr = ', '.join([i for i, j in sub.items() if len(j['grade']) != 0 or len(j['test']) != 0])
#
# print(str_pr)

student = Student("Иван Иванов", "subjects.csv")
print(student)
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)
print(student)
average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")
average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")


student1 = Student("Сидоров Сидор", "subjects.csv")

average_history_score = student1.get_average_test_score("Биология")
