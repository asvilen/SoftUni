number_of_days = int(input())
room_type = input()
rating = input()

discount = 0
price = 0

if room_type == "apartment":
    price = 25.00
    if number_of_days < 10:
        discount = 0.3
    elif number_of_days <= 15:
        discount = 0.35
    elif number_of_days > 15:
        discount = 0.5
elif room_type == "president apartment":
    price = 35.00
    if number_of_days < 10:
        discount = 0.1
    elif number_of_days <= 15:
        discount = 0.15
    elif number_of_days > 15:
        discount = 0.2
else:
    price = 18.00

gross_price = (number_of_days - 1) * price
discount_price = gross_price * (1 - discount)

if rating == "positive":
    final_price = discount_price * 1.25
else:
    final_price = discount_price * (1 - 0.1)

print(f"{final_price:.2f}")