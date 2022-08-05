# Создать класс Triangle, атрибутом которого является лист состоящий из 3-х элементов – сторон треугольника.
# Реализовать метод, который выводит сообщение о возможности построения треугольника или нет.
# *построение возможно если сумма двух меньших сторон больше третьей


class Triangle:
    def __init__(self, sides: list[int]):
        self.sides = sides

    def is_possible(self):
        if sorted(self.sides)[0] + sorted(self.sides)[1] > sorted(self.sides)[2]:
            print("Triangle is possible")
        else:
            print("Triangle is impossible")

    def __str__(self):
        return f"{self.sides}"

sides_1 = [5, 4, 3]
sides_2 = [10, 3, 5]

triang_1 = Triangle(sides_1)
triang_2 = Triangle(sides_2)

triang_1.is_possible()
triang_2.is_possible()
