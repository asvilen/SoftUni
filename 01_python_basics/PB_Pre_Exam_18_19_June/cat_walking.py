walk_minutes = int(input())
walk_count = int(input())
daily_calories = int(input())

burned_cal_per_minute = 5
calories_burned = walk_count * walk_minutes * burned_cal_per_minute

if calories_burned >= daily_calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")