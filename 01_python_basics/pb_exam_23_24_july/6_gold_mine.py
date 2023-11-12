locations = int(input())

for location in range(locations):
    daily_digged_total = 0
    average_daily_gold = float(input())
    days_of_digging = int(input())
    for day in range(days_of_digging):
        digged_for_today = float(input())
        daily_digged_total += digged_for_today
        average_digged = daily_digged_total / days_of_digging
    if average_digged >= average_daily_gold:
        print(f"Good job! Average gold per day: {average_digged:.2f}.")
    else:
        difference = average_daily_gold - average_digged
        print(f"You need {difference:.2f} gold.")