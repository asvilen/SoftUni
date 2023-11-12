from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())
all_stops = amount_of_fuel_needed.copy()
counter = 0
while initial_fuel:
    result = initial_fuel.pop() - additional_consumption_index.popleft()
    needed_fuel = amount_of_fuel_needed.popleft()
    if result >= needed_fuel:
        counter += 1
        print(f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter + 1}")
        break
if counter == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif counter < len(all_stops):
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(['Altitude ' + str(x) for x in range(1, counter + 1)])}")
elif counter == len(all_stops):
    print("John has reached all the altitudes and managed to reach the top!")



