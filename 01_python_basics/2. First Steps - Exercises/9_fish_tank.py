length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

percentage /= 100
volume = length * width * height
volume_in_liters = volume * 0.001

liters_to_fill = volume_in_liters * (1 - percentage)

print(liters_to_fill)
