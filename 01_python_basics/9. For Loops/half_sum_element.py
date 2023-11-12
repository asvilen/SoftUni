import sys

n = int(input())
max_number = -sys.maxsize
sum_total = 0

for number in range(1, n +1):
    current_number = int(input())
    sum_total += current_number

    if current_number > max_number:
        max_number = current_number

sum = sum_total - max_number

if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    difference = abs(sum - max_number)
    print(f"Diff = {difference}")