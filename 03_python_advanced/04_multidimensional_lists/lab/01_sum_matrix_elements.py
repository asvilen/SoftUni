rows, columns = input().split(", ")
matrix = []
total = 0
for row in range(int(rows)):
    current_row = [int(x) for x in input().split(", ")]
    total += sum(current_row)
    matrix.append(current_row)
print(total)
print(matrix)