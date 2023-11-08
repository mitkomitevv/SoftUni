from math import floor


def center_point(x1, y1, x2, y2):
    distance1 = x1 ** 2 + y1 ** 2
    distance2 = x2 ** 2 + y2 ** 2
    if distance1 <= distance2:
        return f'({x1}, {y1})'
    return f'({x2}, {y2})'


x_1, y_1, x_2, y_2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))
print(center_point(x_1, y_1, x_2, y_2))
