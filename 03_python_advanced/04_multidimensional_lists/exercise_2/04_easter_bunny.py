size = int(input())

field = []

for row in range(size):
    field.append([])
    for index, char in enumerate(input().split()):
        field[row].append(char)
        if char == "B":
            bunny_position = [row, index]

possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
max_eggs = float('-inf')
max_path = []
max_direction = None
for current_direction, move in possible_moves.items():
    path = []
    collected_eggs = 0
    new_position = bunny_position
    while True:
        new_position = [new_position[0] + move[0], new_position[1] + move[1]]
        if new_position[0] < 0 or new_position[1] < 0 \
                or new_position[0] >= size or new_position[1] >= size:
            break
        if field[new_position[0]][new_position[1]] == "X":
            break
        path.append(new_position)
        collected_eggs += int(field[new_position[0]][new_position[1]])

    if collected_eggs > max_eggs and path:
        max_eggs = collected_eggs
        max_path = path
        max_direction = current_direction

print(max_direction)
print(*max_path, sep="\n")
print(max_eggs)
