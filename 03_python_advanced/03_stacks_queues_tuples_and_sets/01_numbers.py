first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for commands in range(n):
    line = input().split()
    command, pointer = line[0], line[1]
    numbers = [int(x) for x in line[2:]]
    if command == "Add":
        if pointer == "First":
            first_sequence.update(numbers)
        else:
            second_sequence.update(numbers)
    elif command == "Remove":
        if pointer == "First":
            first_sequence.difference_update(numbers)
        else:
            second_sequence.difference_update(numbers)
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
