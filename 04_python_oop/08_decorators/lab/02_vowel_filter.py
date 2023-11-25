import functools
from debug_decorators.log import log


def vowel_filter(function):
    @functools.wraps(function)
    def wrapper():
        vowels = 'eyuioa'
        result = function()
        return [letter for letter in result if letter in vowels]

    return wrapper


@log
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
