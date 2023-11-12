import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def closest_point(x_1, y_1, x_2, y_2):
    diagonal_1 = math.sqrt(x_1 ** 2 + y_1 ** 2)
    diagonal_2 = math.sqrt(x_2 ** 2 + y_2 ** 2)
    if diagonal_1 > diagonal_2:
        return (int(x_2), int(y_2))
    else:
        return (int(x_1), int(y_1))


print(closest_point(x1, y1, x2, y2))
