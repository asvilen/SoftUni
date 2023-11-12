def valid_corr(m, x_corr, y_corr):
    diapason = range(0, len(m))
    if x_corr in diapason and y_corr in diapason:
        return True
    return False


commands_map = {
    "Add": lambda a, b: a + b,
    "Subtract": lambda a, b: a - b
}

rows = int(input())

matrix = [[int(x) for x in input().split()] for row in range(rows)]

while True:
    command = input().split()
    action = command[0]
    if action == "END":
        break
    x, y, given_number = int(command[1]), int(command[2]), int(command[3])
    if not valid_corr(matrix, x, y):
        print("Invalid coordinates")
        continue

    matrix[x][y] = commands_map[action](matrix[x][y], given_number)

[print(*row, sep=" ") for row in matrix]
