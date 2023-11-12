storage = {}
while True:
    command = input().split()
    if len(command) == 1:
        break
    name, price, quantity = command[0], float(command[1]), int(command[2])
    if name not in storage:
        storage[name] = [0, 0]
    storage[name][0] = price
    storage[name][1] += quantity

for item in storage:
    price = storage[item][0]
    quantity = storage[item][1]
    print(f"{item} -> {(price * quantity):.2f}")