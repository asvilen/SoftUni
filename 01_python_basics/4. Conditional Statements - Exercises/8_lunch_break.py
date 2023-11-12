from math import ceil

series = input()
episode_duration = int(input())
break_duration = int(input())

food_duration = break_duration / 8
rest_duration = break_duration / 4
watching_time_duration = break_duration - food_duration - rest_duration
difference = ceil(abs(watching_time_duration - episode_duration))

if watching_time_duration >= episode_duration:
    print(f"You have enough time to watch {series} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {difference} more minutes.")