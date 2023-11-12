def operate(sign, *args):
    operations_map = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    result = args[0]
    for number in args[1:]:
        result = operations_map[sign](result, number)
    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))