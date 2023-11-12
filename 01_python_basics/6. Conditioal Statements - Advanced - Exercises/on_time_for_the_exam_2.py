exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
difference = exam_time - arrival_time

if 30 >= difference >= 0:
    print("On time")
elif difference > 30:
    print("Early")
else:
    print("Late")

if difference == 0:
    pass
elif 0 < difference < 60:
    print(f"{difference} minutes before the start")
elif difference >= 60:
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:02d} hours before the start")
elif 0 > difference > -60:
    minutes = abs(difference)
    print(f"{minutes} minutes after the start" )
elif difference <= -60:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    print(f"{hours}:{minutes:02d} hours after the start")