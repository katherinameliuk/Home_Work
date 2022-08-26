TEACHER_XP = {"1st stage": [1, 2, 3, 4, 5], "2nd stage": [6, 7, 8, 9]}
TEACHER_1ST_STAGE_K = 1.4
TEACHER_2ND_STAGE_K = 1.6
TEACHER_HIGHEST_STAGE_K = 2
DOCTOR_K = {"beginner": 1.1, "middle": 1.3, "highest": 1.7}


class Worker:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        pass

    def get_salary(self):
        pass


class Doctor(Worker):
    DOCTOR_K = {"beginner": 1.1, "middle": 1.3, "highest": 1.7}

    def __init__(self, salary, category):
        super().__init__(salary)
        self.category = category

    def work(self):
        return "Heal"

    def get_salary(self):
        if self.category == "beginner":
            return f"Salary: {self.salary * DOCTOR_K['beginner']}"
        elif self.category == "middle":
            return f"Salary: {self.salary * DOCTOR_K['middle']}"
        elif self.category == "highest":
            return f"Salary: {self.salary * DOCTOR_K['highest']}"


class Teacher(Worker):

    def __init__(self, salary, xp):
        super().__init__(salary)
        self.xp = xp

    def work(self):
        return "Teach"

    def get_salary(self):
        if self.xp in TEACHER_XP['1st stage']:
            return f"Salary: {self.salary * TEACHER_1ST_STAGE_K}"
        elif self.xp in TEACHER_XP['2nd stage']:
            return f"Salary: {self.salary * TEACHER_2ND_STAGE_K}"
        elif self.xp > 9:
            return f"Salary: {self.salary * TEACHER_HIGHEST_STAGE_K}"


teacher = Teacher(1000, 7)
print(teacher.get_salary())

doctor = Doctor(1000, "middle")
print(doctor.get_salary())
