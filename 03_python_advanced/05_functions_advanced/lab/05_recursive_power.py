def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)

print(recursive_power(2, 10))

print(recursive_power(10, 100))
# def factorial(number):
#     if number == 1:
#         return 1
#     return number * factorial(number - 1)
#
# print(factorial(5))