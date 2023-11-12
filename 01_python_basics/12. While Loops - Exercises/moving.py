width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
taken_space = 0

while free_space > taken_space:
    command = input()
    if command == 'Done':
        break
    boxes = int(command)
    taken_space += boxes

difference = abs(free_space - taken_space)
if command == 'Done':
    print(f"{difference} Cubic meters left.")
if taken_space >= free_space:
    print(f"No more free space! You need {difference} Cubic meters more.")