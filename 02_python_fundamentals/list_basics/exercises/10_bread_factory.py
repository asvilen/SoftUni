energy = 100
coins = 100
order_energy = 30
current_energy = energy
day_events_list = input().split("|")
all_events_completed = True
for event in day_events_list:
    split_event = event.split("-")
    name_ingredients, number = split_event[0], int(split_event[1])
    if name_ingredients == "rest":
        if number + current_energy > energy:
            gained_energy = energy - current_energy
            current_energy = 100
            print(f"You gained {gained_energy} energy.")
        else:
            current_energy += number
        print(f"Current energy: {current_energy}.")
    elif name_ingredients == "order":
        if current_energy < order_energy:
            current_energy += 50
            print("You had to rest!")
            # all_events_completed = False
        else:
            current_energy -= order_energy
            coins += number
            print(f"You earned {number} coins.")
    else:
        if number > coins:
            print(f"Closed! Cannot afford {name_ingredients}.")
            all_events_completed = False
            break
        else:
            coins -= number
            print(f"You bought {name_ingredients}.")
if all_events_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")