rows = int(input())
diagonal_sum = 0
for row in range(rows):
    diagonal_sum += [int(x) for x in input().split()][row]
print(diagonal_sum)
