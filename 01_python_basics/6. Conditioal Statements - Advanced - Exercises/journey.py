budget = float(input())
season = input()

to_spend = 0
spending_factor = 0
vacation_type = ''

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        spending_factor = 0.3
    else:
        spending_factor = 0.7
elif budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        spending_factor = 0.4
    else:
        spending_factor = 0.8
else:
    print("Somewhere in Europe")
    spending_factor = 0.9

if season == "summer" and budget <= 1000:
    vacation_type = "Camp"
else:
    vacation_type = "Hotel"

to_spend = budget * spending_factor

print(f"{vacation_type} - {to_spend:.2f}")