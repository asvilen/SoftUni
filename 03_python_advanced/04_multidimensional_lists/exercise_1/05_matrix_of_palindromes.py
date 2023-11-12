rows, columns = [int(x) for x in input().split()]

starting_letter = 'a'

for row in range(rows):
    row_letter = chr(ord(starting_letter) + row)
    for col in range(columns):
        col_letter = chr(ord(row_letter) + col)
        print(row_letter + col_letter + row_letter, end=' ')
    print()
