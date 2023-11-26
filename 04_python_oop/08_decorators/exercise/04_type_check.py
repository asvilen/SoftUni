import functools


def type_check(input_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if all(isinstance(x, input_type) for x in args):
                return func(*args)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
