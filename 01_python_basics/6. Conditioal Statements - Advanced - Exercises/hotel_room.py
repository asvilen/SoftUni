month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        studio_price *= 0.95
    elif nights > 14:
        studio_price *= 0.7
        apartment_price *= 0.9
elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.7
    if nights > 14:
        studio_price *= 0.8
        apartment_price *= 0.9
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price *= 0.9

apartment_income = apartment_price * nights
studio_income = studio_price * nights
print(f"Apartment: {apartment_income:.2f} lv.")
print(f"Studio: {studio_income:.2f} lv.")