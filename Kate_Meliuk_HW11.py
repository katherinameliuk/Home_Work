# 1. Создать класс User, определить в нем конструктор с полями
# name, surname, age, country, gender, profession.
# Определить вычисляемые методы email, birth_year.
# Затем определить 3 метода, каждый из которых будет создавать экземпляр класса User с определенной профессией
# ( doctor, policeman, teacher).


class User:
    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    def get_email(self):
        email = f"{self.name}, {self.surname}@gmail.com"
        return email

    def get_birth_year(self):
        birth_year = 2022 - int(self.age)
        return birth_year

    def doctor():
        doctor = User("name", "surname", 12, "doctor")
        return doctor

    def policeman():
        policeman = User("name", "surname", 12, "policeman")
        return policeman

    def teacher():
        teacher = User("name", "surname", 12, "teacher")
        return teacher

person_1 = User('alex', 'jhonson', 23, 'doctor')
print(person_1.get_email(), person_1.get_birth_year())

doctor_1 = User.doctor()
print(doctor_1.get_email(), doctor_1.get_birth_year())






