number_of_pages = int(input())
read_pages_per_hour = int(input())
reading_days = int(input())

hours_per_day_reading = number_of_pages / read_pages_per_hour / reading_days

print(int(hours_per_day_reading))