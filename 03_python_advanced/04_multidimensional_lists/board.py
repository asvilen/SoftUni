mat = [[1, 2], [3, 4]]
res = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print(len(set(len(row) for row in mat)) == 1)