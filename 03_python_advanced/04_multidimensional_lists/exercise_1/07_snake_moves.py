from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = input()
snake_path = []

snake_deque = deque(snake)

for row in range(rows):
    snake_path.append([''] * columns)
    for col in range(columns):
        if row % 2 == 0:
            snake_path[row][col] = snake_deque[0]
        else:
            snake_path[row][-col - 1] = snake_deque[0]
        snake_deque.rotate(-1)
[print(*row, sep="") for row in snake_path]

# left_over = ''
# for row in range(rows):
#     characters = left_over + snake
#     if len(characters) < columns:
#         characters += snake
#     this_row = characters[:columns]
#     left_over = characters[columns:]
#     if row % 2 == 0:
#         current_row_path = this_row
#     else:
#         current_row_path = this_row[::-1]
#     snake_path.append(current_row_path)
# print(*snake_path, sep="\n")
