from collections import deque
def position_is_valid(m_size, position):
    diapason = range(m_size)
    if position[0] in diapason and position[1] in diapason:
        return True
    return False


size = int(input())

game_field = [[char for char in input()] for row in range(size)]
knight_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
knights = []

for row in range(size):
    for col in range(size):
        if game_field[row][col] == "K":
            knights.append((row, col))


removed_knights = 0
while True:
    max_hits = 0
    knight_to_remove = None
    for index, knight_position in enumerate(knights):
        hits = 0
        for moves in knight_moves:
            new_position = (knight_position[0] + moves[0], knight_position[1] + moves[1])
            if position_is_valid(size, new_position):
                if game_field[new_position[0]][new_position[1]] == "K":
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            knight_to_remove = index
    if max_hits == 0:
        break
    game_field[knights[knight_to_remove][0]][knights[knight_to_remove][1]] = '0'
    knights.pop(knight_to_remove)
    removed_knights += 1
print(removed_knights)
