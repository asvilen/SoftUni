record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

delay_in_seconds = distance_in_meters // 50 * 30
g_time = distance_in_meters * seconds_per_meter + delay_in_seconds

if g_time < record_in_seconds:
    print(f"Yes! The new record is {g_time:.2f} seconds.")
else:
    difference = g_time - record_in_seconds
    print(f"No! He was {difference:.2f} seconds slower.")