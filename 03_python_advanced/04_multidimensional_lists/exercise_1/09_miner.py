size = int(input())
commands = input().split()
mine = []
total_coal = 0
collected_coal = 0
last_corr = tuple()
game_finished = False

for row in range(size):
    mine.append([])
    for index, value in enumerate(input().split()):
        mine[row].append(value)
        if value == 'c':
            total_coal += 1
        elif value == 's':
            last_corr = (row, index)

movements_map = {
    "up"   : lambda x, y: (x - 1, y),
    "down" : lambda x, y: (x + 1, y),
    "left" : lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

for command in commands:
    new_corr = movements_map[command](last_corr[0], last_corr[1])
    if 0 <= new_corr[0] < len(mine) and 0 <= new_corr[1] < len(mine[0]):
        new_position = mine[new_corr[0]][new_corr[1]]
        last_corr = (new_corr[0], new_corr[1])
        if new_position == 'c':
            mine[new_corr[0]][new_corr[1]] = '*'
            collected_coal += 1
            if collected_coal == total_coal:
                game_finished = True
                print(f"You collected all coal! {last_corr}")
                break
        elif new_position == 'e':
            game_finished = True
            print(f"Game over! {last_corr}")
            break

if not game_finished:
    print(f"{total_coal - collected_coal} pieces of coal left. {last_corr}")
