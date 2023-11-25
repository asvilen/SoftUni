import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        params = [
            ", ".join(str(x) for x in args),
            ", ".join(f"{key}={value}" for key, value in kwargs.items())
        ]
        params_string = ", ".join(params)
        print(f"{func.__name__}({params_string}) = {result}")

        return result

    return wrapper


# @debug
# def my_sum(x, y):
#     return x + y
#
#
# print(my_sum(6, 5))