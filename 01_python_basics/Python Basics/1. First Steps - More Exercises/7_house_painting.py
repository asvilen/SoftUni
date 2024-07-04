from math import sqrt

x = float(input())
y = float(input())
h = float(input())

# Walls of the house
door = 1.2 * 2
window = 1.5 * 1.5
front_and_back_m2 = 2 * x * x - door
left_and_right_m2 = 2 * x * y - (2 * window)
# TOTAL
walls_total = front_and_back_m2 + left_and_right_m2
# Roof of the house
roof_top = 2 * x * y
roof_sides = 2 * x * h / 2
#TOTAL
roof_total = roof_sides + roof_top
#Walls Paint
green_paint = walls_total / 3.4
#Roof Paint
red_paint = roof_total / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")