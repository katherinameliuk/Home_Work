from circle import perimeter_circle, square_circle
from rectangle import perimeter_rectangle, square_rectangle
from triangle import perimeter_triangle, square_triangle



'''parameters = [{'circle': {'square': square_circle(6), perimetr': perimeter_circle(6)}}, {'rectangle': {'square': square_rectangle(3, 5), 'perimetr': perimeter_rectangle(3, 5)}}, {'triangle': {'square': square_triangle(3, 3, 4), 'perimetr': perimeter_triangle(3, 3, 4)}}]
print(parameters, type)'''

def triangle_view(perimeter, square):
    return {"triangle": {"perimeter": perimeter, "square": square}}

def circle_view(perimeter, square):
    return {"circle": {"perimeter": perimeter, "square": square}}

def rectangle_view(perimeter, square):
    return {"rectangle": {"perimeter": perimeter, "square": square}}

print(triangle_view(perimeter=perimeter_triangle(3, 4, 5), square=square_triangle(3, 4, 5)))
print(circle_view(perimeter=perimeter_circle(3), square=square_circle(3)))
print(rectangle_view(perimeter=perimeter_rectangle(3, 4), square=square_rectangle(3, 4)))