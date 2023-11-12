# fruit = input()
# day_of_the_week = input()
# quantity = float(input())
#
# price = 0
#
# if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or day_of_the_week == "Friday":
#     if fruit == 'banana':
#         price = 2.5
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'apple':
#         price = 1.2
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'orange':
#         price = 0.85
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'grapefruit':
#         price = 1.45
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'kiwi':
#         price = 2.7
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'pineapple':
#         price = 5.5
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'grapes':
#         price = 3.85
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     else:
#         print("error")
# elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
#     if fruit == 'banana':
#         price = 2.7
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'apple':
#         price = 1.25
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'orange':
#         price = 0.9
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'grapefruit':
#         price = 1.6
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'kiwi':
#         price = 3
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'pineapple':
#         price = 5.6
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     elif fruit == 'grapes':
#         price = 4.2
#         bill = quantity * price
#         print(f"{bill:.2f}")
#     else:
#         print("error")
# else:
#     print("error")

fruit = input()
day_of_the_week = input()
quantity = float(input())

price = 0

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or day_of_the_week == "Friday":
    if fruit == 'banana':
        price = 2.5
    elif fruit == 'apple':
        price = 1.2
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.7
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if fruit == 'banana':
        price = 2.7
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.9
    elif fruit == 'grapefruit':
        price = 1.6
    elif fruit == 'kiwi':
        price = 3
    elif fruit == 'pineapple':
        price = 5.6
    elif fruit == 'grapes':
        price = 4.2

if price == 0:
    print("error")
else:
    bill = quantity * price
    print(f"{bill:.2f}")