field_size = int(input())
moves = input().split(", ")

matrix = []
collected_hazelnuts = 0
NEEDED_HAZELNUTS = 3
game_over = False

for row in range(field_size):
    matrix.append(list(input()))
    for col in range(field_size):
        if matrix[row][col] == "s":
            s_row = row
            s_col = col
move_map = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for move in moves:
    s_row += move_map[move][0]
    s_col += move_map[move][1]
    if not (0 <= s_row < field_size and 0 <= s_col < field_size):
        print("The squirrel is out of the field.")
        game_over = True
        break
    if matrix[s_row][s_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        game_over = True
        break
    if matrix[s_row][s_col] == "h":
        collected_hazelnuts += 1
        matrix[s_row][s_col] = "*"

if not game_over:
    if collected_hazelnuts == NEEDED_HAZELNUTS:
        print("Good job! You have collected all hazelnuts!")
    else:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")