from math import pi

figure = input()
result = 0

if figure == "square":
    side = float(input())
    result = side ** 2
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
elif figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
else:
    side = float(input())
    height = float(input())
    result = side * height / 2

print(f"{result:.3f}")