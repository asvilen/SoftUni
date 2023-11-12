NUM = 31
sequence_of_strings = input().split()
grand_total = 0
for string in sequence_of_strings:
    current_total = 0
    first_letter = string[0]
    number = int(string[1:-1])
    last_letter = string[-1]
    if first_letter.islower():
        current_total += number * (ord(first_letter) & NUM)
    else:
        current_total += number / (ord(first_letter) & NUM)
    if last_letter.isupper():
        current_total -= (ord(last_letter) & NUM)
    else:
        current_total += (ord(last_letter) & NUM)
    grand_total += current_total
print(f"{grand_total:.2f}")