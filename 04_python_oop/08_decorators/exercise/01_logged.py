import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = func(*args)
        params = ", ".join([str(x) for x in args])
        return (f"you called {func.__name__}({params})\n"
                f"it returned {result}")

    return wrapper


# @logged
# def sum_func(a, b):
#     return a + b
#
#
# print(sum_func(1, 4))
