projection_type = input()
columns = int(input())
rows = int(input())

price = 0
seats_count = rows * columns

if projection_type == "Premiere":
    price = 12.00
elif projection_type == "Normal":
    price = 7.50
elif projection_type == "Discount":
    price = 5.00

income = seats_count * price
print(f"{income:.2f} leva")