trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sum_puzzles = puzzles * 2.6
sum_dolls = dolls * 3
sum_bears = bears * 4.1
sum_minions = minions * 8.2
sum_trucks = trucks * 2

count = puzzles + dolls + bears + minions + trucks
total_sum = sum_puzzles + sum_dolls + sum_bears + sum_minions + sum_trucks

if count >= 50:
    total_sum -= total_sum * 0.25

total_sum -= total_sum * 0.1
difference = abs(trip_price - total_sum)

if total_sum >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")