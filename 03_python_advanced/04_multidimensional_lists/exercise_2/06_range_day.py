size = 5

shooting_field = []
my_position = []
targets = 0
hit_targets = []
for row in range(size):
    shooting_field.append(input().split())
    for col in range(size):
        if not my_position:
            if shooting_field[row][col] == "A":
                my_position = [row, col]
        if shooting_field[row][col] == "x":
            targets += 1

possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

number_of_commands = int(input())
for command in range(number_of_commands):
    current_command = input().split()
    action = current_command[0]
    direction = current_command[1]

    if action == "shoot":
        s_row = my_position[0] + possible_moves[direction][0]
        s_col = my_position[1] + possible_moves[direction][1]
        while 0 <= s_row < size and 0 <= s_col < size:
            if shooting_field[s_row][s_col] == "x":
                shooting_field[s_row][s_col] = "."
                hit_targets.append([s_row, s_col])
                targets -= 1
                break
            s_row += possible_moves[direction][0]
            s_col += possible_moves[direction][1]
        if targets == 0:
            print(f"Training completed! All {len(hit_targets)} targets hit.")
            break
    elif action == "move":
        steps = int(current_command[-1])
        m_row = my_position[0] + possible_moves[direction][0] * steps
        m_col = my_position[1] + possible_moves[direction][1] * steps
        if 0 <= m_row < size and 0 <= m_col < size and shooting_field[m_row][m_col] == ".":
            shooting_field[m_row][m_col] = "A"
            shooting_field[my_position[0]][my_position[1]] = "."
            my_position = [m_row, m_col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(target) for target in hit_targets]
