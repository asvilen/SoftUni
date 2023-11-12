from collections import deque


def calculator(list_of_nums, operation):
    result = list_of_nums.popleft()
    while list_of_nums:
        if operation == "+":
            result += list_of_nums.popleft()
        elif operation == "-":
            result -= list_of_nums.popleft()
        elif operation == "*":
            result *= list_of_nums.popleft()
        elif operation == "/":
            result /= list_of_nums.popleft()
    return int(result)


expression = input().split()

operators = "+-*/"
numbers = deque()

for char in expression:
    if char not in operators:
        numbers.append(int(char))
    else:
        operation_result = calculator(numbers, char)
        numbers.append(operation_result)
print(*numbers)
