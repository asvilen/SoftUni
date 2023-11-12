size = int(input())

matrix = []
for row in range(size):
    matrix.append(input())

special_symbol = input()
symbol_found = False
position = ()

for row in range(size):
    if symbol_found:
        break
    for index in range(len(matrix[row])):
        if special_symbol == matrix[row][index]:
            symbol_found = True
            position = (row, index)
            break
if symbol_found:
    print(position)
else:
    print(f"{special_symbol} does not occur in the matrix")