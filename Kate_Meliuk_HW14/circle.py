from math import pi

def perimeter_circle(r: float):
    perimeter_circle = 2 * pi * r
    return perimeter_circle


def square_circle(r: float):
    square_circle = pi * r**2
    return square_circle


if __name__ == '__main__':
    print(perimeter_circle(3))
    print(square_circle(3))