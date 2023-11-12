toy_price = 5
sweater_price = 15
toys = 0
sweaters = 0

while True:
    command = input()
    if command == "Christmas":
        break
    current_member_age = int(command)
    if current_member_age > 16:
        sweaters += 1
    else:
        toys += 1

toys_sum = toys * toy_price
sweater_sum = sweater_price * sweaters

print(f"Number of adults: {sweaters}")
print(f"Number of kids: {toys}")
print(f"Money for toys: {toys_sum}")
print(f"Money for sweaters: {sweater_sum}")