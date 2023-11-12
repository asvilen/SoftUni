rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

largest_sum = float('-inf')

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = 0
        current_submatrix = []
        for el in range(3):
            current_sum += matrix[row + el][column] + matrix[row + el][column + 1] + matrix[row + el][column + 2]
            current_submatrix.append([matrix[row + el][column], matrix[row + el][column + 1], matrix[row + el][column + 2]])
        if current_sum > largest_sum:
            largest_sum = current_sum
            submatrix = current_submatrix

print(f"Sum = {largest_sum}")
for row in submatrix:
    print(*row, sep=" ")
