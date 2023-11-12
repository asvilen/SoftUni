goal = 10000
steps = 0
total_steps = 0

while total_steps < goal:
    command = input()
    if command == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        break
    steps = int(command)
    total_steps += steps


difference = abs(total_steps - goal)
if total_steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")