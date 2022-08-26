def perimeter_triangle(a: float, b: float, c: float):
    return sum((a, b, c))


def square_triangle(a: float, b: float, c: float):
    perimetr = 0.5 * perimeter_triangle(a, b, c)
    square_triangle = (perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c)) ** 0.5
    return square_triangle


if __name__ == '__main__':
    print(perimeter_triangle(3, 4, 5))
    print(square_triangle(3, 4, 5))
