rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

largest_sum = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current_sum = matrix[row][column] + matrix[row][column + 1] + matrix[row + 1][column] + matrix[row + 1][column + 1]
        if current_sum > largest_sum:
            largest_sum = current_sum
            submatrix = [
                [matrix[row][column], matrix[row][column + 1]],
                [matrix[row + 1][column], matrix[row + 1][column + 1]]
            ]
for row in submatrix:
    print(*row, sep=" ")
print(largest_sum)
