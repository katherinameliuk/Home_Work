# Построить иерархию классов, удовлетворяющую следующим условиям (тематика иерархии на ваше усмотрение):
#- Количество классов >= 5.
#- Использовать наследование, в т.ч. множественное
#- Для каждого класса определить минимум 4 магических метода (на ваш выбор)
#- Создать экземпляры для каждого класса
#-  Иерархия должна быть логичной и не противоречить принципам ООП.

from dataclasses import dataclass


@dataclass
class Shape:
    pass


@dataclass
class FlatShape(Shape):
    square: float

    def get_square(self):
        return None


@dataclass
class VolumetricShape(Shape):
    volume: float

    def get_volume(self):
        return  None


@dataclass
class Circle(FlatShape):
    radius: float

    def get_square(self):
        return 3.14 * self.radius ** 2


@dataclass
class Rectangle(FlatShape):
    side_a: float
    side_b: float

    def get_square(self):
        return self.side_a * self.side_b


@dataclass
class Cube(VolumetricShape):
    side: float

    def get_volume(self):
        return self.side ** 3


@dataclass
class Sphere(VolumetricShape, Circle):

    def get_volume(self):
        return f"{4/3 * 3.14 * self.radius ** 3:.2f}"

    def get_square(self):
        return "Sphere square"


shape = Shape()
flat_shape = FlatShape(None)
volumetric_shape = VolumetricShape(None)

circle = Circle(square=None, radius=3)
rectangle = Rectangle(square=None, side_a=4, side_b=33.5)
cube = Cube(volume=None, side=3)
sphere = Sphere(square=None, radius=12, volume=None)

print(circle.get_square(), rectangle.get_square(), cube.get_volume(), sphere.get_volume(), sphere.get_square())

