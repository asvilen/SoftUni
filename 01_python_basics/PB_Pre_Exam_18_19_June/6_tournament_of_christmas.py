number_of_days = int(input())

loses_counter = 0
wins_counter = 0
daily_charity = 0
total_charity = 0
days_won = 0

for days in range(number_of_days):
    command = input()
    while command != "Finish":
        result = input()
        if result == "win":
            daily_charity += 20
            wins_counter += 1
        else:
            loses_counter += 1
        command = input()
    if wins_counter > loses_counter:
        total_charity += daily_charity * 1.1
        days_won += 1
    else:
        total_charity += daily_charity
    loses_counter = 0
    wins_counter = 0
    daily_charity = 0

if days_won > number_of_days / 2:
    total_charity *= 1.2
    print(f"You won the tournament! Total raised money: {total_charity:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_charity:.2f}")