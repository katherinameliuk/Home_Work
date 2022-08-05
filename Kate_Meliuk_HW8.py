# Напишите программу с классом Car.
# Создайте конструктор (__init__) класса Car.
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите три метода для этого класса.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий - магический метод str  для вывода атрибутов экземпляра в виде строки.
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def __str__(self) -> str:
        return f'Color: {self.color}, Type: {self.type}, Year: {self.year}'

    def start(self):
        return print("Car is started")
    def finish(self):
        return print("Car is finish")


tesla = Car("white", "sedan", "2022")
tesla.start()
tesla.finish()
print(tesla)