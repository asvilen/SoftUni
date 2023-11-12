sum_of_money = 0
instalment = input()

while instalment != 'NoMoreMoney':
    instalment = float(instalment)
    if instalment < 0:
        print(f"Invalid operation!")
        break
    sum_of_money += instalment
    print(f"Increase: {instalment:.2f}")
    instalment = input()

print(f"Total: {sum_of_money:.2f}")