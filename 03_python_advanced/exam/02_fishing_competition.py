size = int(input())

QUOTA = 20
matrix = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "S":
            matrix[row][col] = "-"
            s_row = row
            s_col = col

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

collected_fish = 0
whirlpool = False

while True:

    command = input()
    if command == "collect the nets":
        break

    new_row = s_row + moves[command][0]
    new_col = s_col + moves[command][1]

    if not (0 <= new_row < size and 0 <= new_col < size):
        if command == "up":
            new_row = size - 1
        elif command == "down":
            new_row = 0
        elif command == "left":
            new_col = size - 1
        elif command == "right":
            new_col = 0

    matrix[s_row][s_col] = "-"
    s_row = new_row
    s_col = new_col

    try:
        collected_fish += int(matrix[s_row][s_col])
    except ValueError:
        pass
    if matrix[s_row][s_col] == "W":
        whirlpool = True
        break
    # Update last position
    matrix[s_row][s_col] = "S"

if whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{s_row},{s_col}]")
else:
    if collected_fish >= QUOTA:
        print("Success! You managed to reach the quota!")
    elif collected_fish < QUOTA:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - collected_fish} tons of fish more.")
    if collected_fish > 0:
        print(f"Amount of fish caught: {collected_fish} tons.")
    [print(*row, sep="") for row in matrix]
