import functools
from debug_decorators.debug import debug


def multiply(times):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs) * times

        return wrapper

    return decorator


@debug
@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
