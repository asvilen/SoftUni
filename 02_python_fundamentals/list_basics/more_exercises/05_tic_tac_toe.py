first_line = [int(num) for num in input().split()]
second_line = [int(num) for num in input().split()]
third_line = [int(num) for num in input().split()]
all_lines_list = [first_line, second_line, third_line]
result = 0
for line in range(3):
    if all_lines_list[line][0] == all_lines_list[line][1] == all_lines_list[line][2]:
        result = all_lines_list[line][0]
        break
    if all_lines_list[0][line] == all_lines_list[1][line] == all_lines_list[2][line]:
        result = all_lines_list[0][line]
        break
if all_lines_list[0][0] == all_lines_list[1][1] == all_lines_list[2][2]:
    result = all_lines_list[0][0]
if all_lines_list[0][2] == all_lines_list[1][1] == all_lines_list[2][0]:
    result = all_lines_list[0][2]

if result == 1:
    print("First player won")
elif result == 2:
    print("Second player won")
elif result == 0:
    print("Draw!")

