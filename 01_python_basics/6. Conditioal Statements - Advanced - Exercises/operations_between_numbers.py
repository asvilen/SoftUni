number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0
zero = False
number_type = False
even_odd = 3

if operator == "+":
    result = number_1 + number_2
    even_odd = result % 2
    number_type = True
elif operator == "-":
    result = number_1 - number_2
    even_odd = result % 2
    number_type = True
elif operator == "*":
    result = number_1 * number_2
    even_odd = result % 2
    number_type = True
elif operator == "/":
    if number_2 != 0:
        result = number_1 / number_2
    else:
        zero = True
elif operator == "%":
    if number_2 != 0:
        result = number_1 % number_2
    else:
        zero = True

if  zero == True:
    print(f"Cannot divide {number_1} by zero")
elif even_odd == 0 and number_type == True:
    print(f"{number_1} {operator} {number_2} = {result} - even")
elif even_odd == 1  and number_type == True:
    print(f"{number_1} {operator} {number_2} = {result} - odd")
elif operator == "/":
    print(f"{number_1} {operator} {number_2} = {result:.2f}")
elif operator == "%":
    print(f"{number_1} {operator} {number_2} = {result}")