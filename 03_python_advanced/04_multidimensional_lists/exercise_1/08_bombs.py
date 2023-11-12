size = int(input())
mine_field = [[int(x) for x in input().split()] for row in range(size)]

coordinates = input().split()

neighbour_map = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for bomb in coordinates:
    x, y = [int(corr) for corr in bomb.split(",")]
    power = mine_field[x][y]
    if power > 0:
        for n_x_corr, n_y_corr in neighbour_map:
            x_to_exp = x + n_x_corr
            y_to_exp = y + n_y_corr
            if 0 <= x_to_exp <= len(mine_field) - 1 \
                    and 0 <= y_to_exp <= len(mine_field[0]) - 1:
                if mine_field[x_to_exp][y_to_exp] > 0:
                    mine_field[x_to_exp][y_to_exp] -= power
        mine_field[x][y] = 0

active_cells = []
for row in mine_field:
    [active_cells.append(x) for x in row if x > 0]

print(f"Alive cells: {len(active_cells)}")
print(f"Sum: {sum(active_cells)}")
[print(*row, sep=" ") for row in mine_field]
