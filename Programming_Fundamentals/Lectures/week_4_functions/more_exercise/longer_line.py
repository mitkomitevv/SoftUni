from math import floor, sqrt


def cartesian_line(a, b, c, d):
    point1 = floor(sqrt(a ** 2 + b ** 2))
    point2 = floor(sqrt(c ** 2 + d ** 2))
    line = point1 + point2
    return line, point1, point2


x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
x_3, y_3, x_4, y_4 = int(input()), int(input()), int(input()), int(input())
line1, point_x, point_y = cartesian_line(x_1, y_1, x_2, y_2)
line2, point_z, point_v = cartesian_line(x_3, y_3, x_4, y_4)
if line1 >= line2:
    if abs(point_x) <= abs(point_y):
        print(f'({x_1}, {y_1})({x_2}, {y_2})')
    else:
        print(f'({x_2}, {y_2})({x_1}, {y_1})')
else:
    if abs(point_z) <= abs(point_v):
        print(f'({x_3}, {y_3})({x_4}, {y_4})')
    else:
        print(f'({x_4}, {y_4})({x_3}, {y_3})')
