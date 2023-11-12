age = int(input())
washer_price = float(input())
toy_price = int(input())

toy_count = 0
savings = 0
saved = 10
brother_stolen = 0

for year in range(1, age+1):
    if year % 2 == 0:
        savings += saved
        saved += 10
        brother_stolen += 1
    else:
        toy_count += 1
net_worth = savings - brother_stolen + toy_price * toy_count
difference = net_worth - washer_price
if difference >= 0:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {abs(difference):.2f}")