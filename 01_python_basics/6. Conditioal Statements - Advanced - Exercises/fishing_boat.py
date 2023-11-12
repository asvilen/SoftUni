budget = int(input())
season = input()
fishermen = int(input())

boat_cost = 0
discount = 0
final_price = 0

#Намираме цената на лодката
if season == "Spring":
    boat_cost = 3000
elif season == "Winter":
    boat_cost = 2600
else:
    boat_cost = 4200
#Определяме отстъпката
if fishermen <= 6:
    discount = 0.1
elif fishermen <= 11:
    discount = 0.15
elif fishermen > 12:
    discount = 0.25

#Изчисляваме крайната сума и разликата между крайната сума и бюджета
d_price = boat_cost * (1 - discount)
if fishermen % 2 == 0 and season != "Autumn":
    final_price = d_price * (1 - 0.05)
else:
    final_price = d_price
difference = abs(budget - final_price)

#Проверяваме дали парите са стигнали и отпечатваме резултата
if final_price <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")