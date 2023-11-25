import functools


def log(func):
    @functools.wraps(func)
    def wrapper():
        print(f"{func.__name__} executed")
        return func()

    return wrapper


# @logg-
# def f1():
#     return 5
#
#
# print(f1())
