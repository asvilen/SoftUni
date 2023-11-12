length = int(input())
width = int(input())

cake = length * width
eaten_pieces = 0

while cake >= eaten_pieces:
    command = input()
    if command == 'STOP':
        break
    current_eaten = int(command)
    eaten_pieces += current_eaten


difference = abs(cake - eaten_pieces)

if command == 'STOP':
    print(f"{difference} pieces are left.")
if eaten_pieces >= cake:
    print(f"No more cake left! You need {difference} pieces more.")