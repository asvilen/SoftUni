savings = float(input())
sex = input()
age = int(input())
sport_type = input()

price = 0

if sex == "m":
    if sport_type == "Gym":
        price = 42
    elif sport_type == "Boxing":
        price = 41
    elif sport_type == "Yoga":
        price = 45
    elif sport_type == "Zumba":
        price = 34
    elif sport_type == "Dances":
        price = 51
    elif sport_type == "Pilates":
        price = 39
else:
    if sport_type == "Gym":
        price = 35
    elif sport_type == "Boxing":
        price = 37
    elif sport_type == "Yoga":
        price = 42
    elif sport_type == "Zumba":
        price = 31
    elif sport_type == "Dances":
        price = 53
    elif sport_type == "Pilates":
        price = 37
if age <= 19:
    price *= 0.8
if price <= savings:
    print(f"You purchased a 1 month pass for {sport_type}.")
else:
    difference = price - savings
    print(f"You don't have enough money! You need ${difference:.2f} more.")