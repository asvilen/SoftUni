def func_executor(*args):
    resulting_list = []
    for pair in args:
        function_name = pair[0]
        function_arguments = pair[1]
        result = function_name(*function_arguments)
        resulting_list.append(f"{function_name.__name__} - {result}")
    return "\n".join(resulting_list)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
