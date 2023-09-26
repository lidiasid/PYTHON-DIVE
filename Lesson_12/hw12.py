""" Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых."""


import csv
from functools import lru_cache

class CapitalizedString:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not value[0].isupper() or not value.isalpha():
            raise ValueError(f"Неверный формат: {value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, "")

class Student:
    first_name = CapitalizedString()
    last_name = CapitalizedString()
    middle_name = CapitalizedString()

    def __init__(self, first_name, last_name, middle_name, csv_file):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.subjects = self._load_subjects_from_csv(csv_file)

    @staticmethod
    @staticmethod
    @staticmethod
    def _load_subjects_from_csv(csv_file):
        subjects = {}
        try:
            with open(csv_file, "r", encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(f"Загружен предмет: {row[0]}")  # Для отладки
                    subjects[row[0]] = {"grades": [], "test_scores": []}
        except Exception as e:
            raise RuntimeError(f"Не удалось загрузить CSV: {e}")
        return subjects

    def _validate_subject(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")

    def add_grade(self, subject, grade):
        self._validate_subject(subject)
        if 2 <= grade <= 5:
            self.subjects[subject]["grades"].append(grade)
        else:
            raise ValueError("Оценка должна быть от 2 до 5")

    def add_test_score(self, subject, score):
        self._validate_subject(subject)
        if 0 <= score <= 100:
            self.subjects[subject]["test_scores"].append(score)
        else:
            raise ValueError("Баллы должны быть от 0 до 100")

    @lru_cache(maxsize=None)
    def avg_test_score(self, subject):
        self._validate_subject(subject)
        scores = self.subjects[subject]["test_scores"]
        return sum(scores) / len(scores) if scores else 0

    @lru_cache(maxsize=None)
    def avg_grade(self):
        all_grades = [grade for subject in self.subjects.values() for grade in subject["grades"]]
        return sum(all_grades) / len(all_grades) if all_grades else 0


s = Student("Иван", "Иванов", "Иванович", r"c:\Users\lida1\Desktop\Python dive\Lesson_12\subjects.csv")
s.add_grade("Математика", 4)
s.add_grade("Математика", 5)
s.add_test_score("Математика", 90)
s.add_test_score("Математика", 85)

print(s.avg_test_score("Математика"))  
print(s.avg_grade())  
