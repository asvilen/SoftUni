from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])

collected_honey = 0

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while working_bees and nectar:
    current_nectar = nectar.pop()
    if working_bees[0] <= current_nectar:
        current_bee = working_bees.popleft()
        current_symbol = symbols.popleft()
        if current_symbol == "/" and current_nectar == 0:
            pass
        else:
            collected_honey += abs(operations[current_symbol](current_bee, current_nectar))

print(f"Total honey made: {collected_honey}")
if working_bees:
    print(f"Bees left: ", end="")
    print(*working_bees, sep=", ")
if nectar:
    print(f"Nectar left: ", end="")
    print(*nectar, sep=", ")

