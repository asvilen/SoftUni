vacation_price = float(input())
savings = float(input())

spend_counter = 0
total_days = 0

while savings < vacation_price and spend_counter < 5:
    action = input()
    amount = float(input())
    total_days += 1
    if action == 'spend':
        savings -= amount
        spend_counter += 1
        if savings < 0:
            savings = 0
    else:
        savings += amount
        spend_counter = 0

if spend_counter == 5:
    print(f"You can't save the money.")
    print(total_days)
if savings >= vacation_price:
    print(f"You saved the money for {total_days} days.")