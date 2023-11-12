first = int(input())
second = int(input())
third = int(input())


def get_sign(one, two, three):
    result = "positive"
    for number in [one, two, three]:
        if number == 0:
            return "zero"
        elif number < 0:
            if result == "negative":
                result = "positive"
            else:
                result = "negative"
    return result


print(get_sign(first, second, third))
