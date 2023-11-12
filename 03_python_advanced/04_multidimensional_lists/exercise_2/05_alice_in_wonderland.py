size = int(input())

territory = []
alice = []
for row in range(size):
    territory.append([x for x in input().split()])
    if not alice:
        for col in range(size):
            if territory[row][col] == "A":
                alice = [row, col]
                territory[row][col] = "*"

possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

row = alice[0]
col = alice[1]
tea_bags = 0
ready = False

while True:
    direction = input()
    current_move = possible_moves[direction]
    row += current_move[0]
    col += current_move[1]
    if row < 0 or row == size or col < 0 or col == size:
        break
    if territory[row][col] == "R":
        territory[row][col] = "*"
        break

    elif territory[row][col] not in ".*":
        tea_bags += int(territory[row][col])

    territory[row][col] = "*"

    if tea_bags >= 10:
        ready = True
        break

if ready:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row, sep=" ") for row in territory]
