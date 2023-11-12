rows, columns = input().split(", ")
matrix = []
for row in range(int(rows)):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for column in range(int(columns)):
    column_total = 0
    for row in range(int(rows)):
        column_total += matrix[row][column]
    print(column_total)
