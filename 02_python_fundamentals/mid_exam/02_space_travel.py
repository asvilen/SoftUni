route_to_titan = input().split("||")
# commands_list = [route.split()[0] for route in route_to_titan]
# numbers_list = [int(route.split()[1]) for route in route_to_titan if route.split()[0] != "Titan"]
# print(commands_list)
# print(numbers_list)

fuel = int(input())
ammunition = int(input())

for route in route_to_titan:
    command = route.split()[0]
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    number = int(route.split()[1])
    if command == "Travel":
        if fuel >= number:
            fuel -= number
            print(f"The spaceship travelled {number} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        if ammunition >= number:
            ammunition -= number
            print(f"An enemy with {number} armour is defeated.")
        else:
            fuel -= number * 2
            if fuel >= 0:
                print(f"An enemy with {number} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif command == "Repair":
        fuel += number
        ammunition += number * 2
        print(f"Ammunitions added: {number * 2}.")
        print(f"Fuel added: {number}.")
