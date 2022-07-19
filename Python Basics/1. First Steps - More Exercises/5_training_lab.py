w = float(input())
h = float(input())
w *= 100
h = h * 100 - 100

columns_of_places = h // 70
rows_of_places = w // 120
total_places = columns_of_places * rows_of_places - 3

print(int(total_places))