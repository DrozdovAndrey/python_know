import csv


class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = dict()
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f, dialect='excel')
            for line in csv_file:
                for i in line:
                    self.subjects[i] = {'grade': [], 'test': []}



