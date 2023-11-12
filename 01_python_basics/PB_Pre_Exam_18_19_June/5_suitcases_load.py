capacity = float(input())
command = input()

current_luggage = 0
luggage_counter = 0
full = False

while command != "End":
    current_luggage = float(command)
    if (luggage_counter + 1) % 3 == 0:
        capacity -= current_luggage * 1.1
    else:
        capacity -= current_luggage
    if capacity <= 0:
        full = True
        break
    luggage_counter += 1
    command = input()

if full:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {luggage_counter} suitcases loaded.")