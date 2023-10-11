from math import floor, sqrt


def cartesian_line(a, b, c, d):
    point1 = sqrt(a ** 2 + b ** 2)
    point2 = sqrt(c ** 2 + d ** 2)
    line = point1 + point2
    return line, point1, point2


x_1, y_1, x_2, y_2 = float(input()), float(input()), float(input()), float(input())
x_3, y_3, x_4, y_4 = float(input()), float(input()), float(input()), float(input())
line1, point_x, point_y = cartesian_line(x_1, y_1, x_2, y_2)
line2, point_z, point_v = cartesian_line(x_3, y_3, x_4, y_4)
if line1 >= line2:
    if abs(point_x) <= abs(point_y):
        print(f'({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})')
    else:
        print(f'({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})')
else:
    if abs(point_z) <= abs(point_v):
        print(f'({floor(x_3)}, {floor(y_3)})({floor(x_4)}, {floor(y_4)})')
    else:
        print(f'({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})')
