start = int(input())
stop = int(input())
magic_number = int(input())


counter = 0
number1 = 0
number2 = 0

for number1 in range(start,stop + 1):
    for number2 in range(start,stop + 1):
        counter += 1
        if number1 + number2 == magic_number:
            break
    if number1 + number2 == magic_number:
        break
if number1 + number2 == magic_number:
    print(f"Combination N:{counter} ({number1} + {number2} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")