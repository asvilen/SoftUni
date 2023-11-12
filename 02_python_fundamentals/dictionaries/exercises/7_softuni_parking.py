number_of_entries = int(input())
parking_lot = {}
for current_entry in range(number_of_entries):
    command = input().split()
    if len(command) == 3:
        username, licence_plate = command[1], command[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {licence_plate}")
        else:
            parking_lot[username] = licence_plate
            print(f"{username} registered {licence_plate} successfully")
    else:
        username = command[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking_lot.pop(username)
for driver in parking_lot:
    print(f"{driver} => {parking_lot[driver]}")