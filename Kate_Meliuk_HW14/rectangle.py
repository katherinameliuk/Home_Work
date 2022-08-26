def perimeter_rectangle(a: float, b: float):
    perimeter_rectangle = (a + b) * 2
    return perimeter_rectangle


def square_rectangle(a: float, b: float):
    square_rectangle = a * b
    return square_rectangle


if __name__ == '__main__':
    print(perimeter_rectangle(3, 5))
    print(square_rectangle(3, 5))