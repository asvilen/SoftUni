exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
difference = exam_time - arrival_time
abs_difference = abs(exam_time - arrival_time)
hour = abs(exam_hour - arrival_hour)
minute = abs(exam_minute - arrival_minute)

if difference < 0:
    print("Late")
elif 30 >= difference >= 0:
    print("On time")
else:
    print("Early")

if -60 < difference < 0:
    print(f"{abs_difference} minutes after the start")
elif difference == 0:
    pass
elif 0 < difference < 60:
    print(f"{abs_difference} minutes before the start")
elif difference >= 60:
    print(f"{hour}:{minute:02d} hours before the start")
else:
    print(f"{hour}:{minute:02d} hours after the start")
