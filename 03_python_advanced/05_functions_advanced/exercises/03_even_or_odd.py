def even_odd(*args):
    command = args[-1]
    if command == "even":
        numbers = [int(x) for x in args[:-1] if x % 2 == 0]
    else:
        numbers = [int(x) for x in args[:-1] if x % 2 != 0]
    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
