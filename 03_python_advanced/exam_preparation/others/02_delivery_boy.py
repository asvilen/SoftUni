n, m = [int(x) for x in input().split()]

matrix = []


for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "B":
            starting_row = row
            starting_col = col

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

current_row = starting_row
current_col = starting_col

while True:
    command = input()
    new_row = current_row + moves[command][0]
    new_col = current_col + moves[command][1]
    if 0 <= new_row < n and 0 <= new_col < m:
        if matrix[new_row][new_col] == "*":
            continue
        current_row = new_row
        current_col = new_col
        if matrix[current_row][current_col] == "P":
            matrix[current_row][current_col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
        elif matrix[current_row][current_col] == "A":
            matrix[current_row][current_col] = "P"
            print("Pizza is delivered on time! Next order...")
            break
        elif matrix[current_row][current_col] == "-":
            matrix[current_row][current_col] = "."
    else:
        print("The delivery is late. Order is canceled.")
        matrix[starting_row][starting_col] = " "
        break

[print(*row, sep="") for row in matrix]