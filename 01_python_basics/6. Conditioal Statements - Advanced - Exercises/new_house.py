flower_type = input()
amount = int(input())
budget = int(input())

price = 0
discount = 0
markup = 0

if flower_type == "Roses":
    price = 5
    if amount > 80:
        discount = 0.1
    bill = price * amount * (1 - discount)
elif flower_type == "Dahlias":
    price = 3.8
    if amount > 90:
        discount = 0.15
    bill = price * amount * (1 - discount)
elif flower_type == "Tulips":
    price = 2.8
    if amount > 80:
        discount = 0.15
    bill = price * amount * (1 - discount)
elif flower_type == "Narcissus":
    price = 3
    if amount < 120:
        markup = 0.15
    bill = price * amount * (1 + markup)
elif flower_type == "Gladiolus":
    price = 2.5
    if amount < 80:
        markup = 0.2
    bill = price * amount * (1 + markup)

difference = abs(bill - budget)

if bill > budget:
    print(f"Not enough money, you need {difference:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {amount} {flower_type} and {difference:.2f} leva left.")