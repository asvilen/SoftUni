starting_num_of_presents = int(input())
num_left_presents = starting_num_of_presents
size = int(input())
neighbourhood = []
santa = []
good_kids = 0

for row in range(size):
    neighbourhood.append(input().split())
    for col in range(size):
        if not santa:
            if neighbourhood[row][col] == "S":
                santa = [row, col]
        if neighbourhood[row][col] == "V":
            good_kids += 1

possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

good_kids_left = good_kids

while num_left_presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    new_row = santa[0] + possible_moves[command][0]
    new_col = santa[1] + possible_moves[command][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        neighbourhood[santa[0]][santa[1]] = "-"
        santa[0] = new_row
        santa[1] = new_col
        if neighbourhood[new_row][new_col] == "V":
            num_left_presents -= 1
            good_kids_left -= 1
        elif neighbourhood[new_row][new_col] == "C":
            for move in possible_moves.values():
                happy_row = new_row + move[0]
                happy_col = new_col + move[1]
                if neighbourhood[happy_row][happy_col] == "X":
                    neighbourhood[happy_row][happy_col] = "-"
                    num_left_presents -= 1
                elif neighbourhood[happy_row][happy_col] == "V":
                    neighbourhood[happy_row][happy_col] = "-"
                    num_left_presents -= 1
                    good_kids_left -= 1
        neighbourhood[new_row][new_col] = "S"

if good_kids_left > 0 and num_left_presents == 0:
    print("Santa ran out of presents!")

[print(*row) for row in neighbourhood]

if good_kids_left > 0:
    print(f"No presents for {good_kids_left} nice kid/s.")
else:
    print(f"Good job, Santa! {good_kids} happy nice kid/s.")

