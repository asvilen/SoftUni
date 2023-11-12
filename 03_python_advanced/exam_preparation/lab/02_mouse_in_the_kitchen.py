n, m = [int(x) for x in input().split(",")]

matrix = []
num_of_cheese = 0

for row in range(n):
    matrix.append([char for char in input()])
    for col in range(m):
        if matrix[row][col] == "M":
            matrix[row][col] = "*"
            mouse_row = row
            mouse_col = col
        elif matrix[row][col] == "C":
            num_of_cheese += 1

movement_map = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break
    new_row = mouse_row + movement_map[command][0]
    new_col = mouse_col + movement_map[command][1]
    if 0 <= new_row < n and 0 <= new_col < m:
        if matrix[new_row][new_col] == "@":
            continue
        mouse_row = new_row
        mouse_col = new_col
        if matrix[mouse_row][mouse_col] == "C":
            num_of_cheese -= 1
            matrix[mouse_row][mouse_col] = "*"
            if num_of_cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        elif matrix[mouse_row][mouse_col] == "T":
            print("Mouse is trapped!")
            break
    else:
        print("No more cheese for tonight!")
        break
matrix[mouse_row][mouse_col] = "M"
[print(*row, sep="") for row in matrix]
