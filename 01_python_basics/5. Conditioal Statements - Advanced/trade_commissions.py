# city = input()
# sales_volume = float(input())
#
# if city == 'Sofia':
#     if sales_volume <= 0:
#         print("error")
#     elif sales_volume <= 500:
#         commission = sales_volume * 0.05
#         print(f"{commission:.2f}")
#     elif sales_volume <= 1000:
#         commission = sales_volume * 0.07
#         print(f"{commission:.2f}")
#     elif sales_volume <= 10000:
#         commission = sales_volume * 0.08
#         print(f"{commission:.2f}")
#     elif sales_volume > 1000:
#         commission = sales_volume * 0.12
#         print(f"{commission:.2f}")
#
# elif city == 'Varna':
#     if sales_volume <= 0:
#         print("error")
#     elif sales_volume <= 500:
#         commission = sales_volume * 0.045
#         print(f"{commission:.2f}")
#     elif sales_volume <= 1000:
#         commission = sales_volume * 0.075
#         print(f"{commission:.2f}")
#     elif sales_volume <= 10000:
#         commission = sales_volume * 0.1
#         print(f"{commission:.2f}")
#     elif sales_volume > 1000:
#         commission = sales_volume * 0.13
#         print(f"{commission:.2f}")
#
# elif city == 'Plovdiv':
#     if sales_volume <= 0:
#         print("error")
#     elif sales_volume <= 500:
#         commission = sales_volume * 0.055
#         print(f"{commission:.2f}")
#     elif sales_volume <= 1000:
#         commission = sales_volume * 0.08
#         print(f"{commission:.2f}")
#     elif sales_volume <= 10000:
#         commission = sales_volume * 0.12
#         print(f"{commission:.2f}")
#     elif sales_volume > 1000:
#         commission = sales_volume * 0.145
#         print(f"{commission:.2f}")
# else:
#     print("error")

city = input()
sales = float(input())

commission = 0

if 0 < sales <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.1
    elif city == "Plovdiv":
        commission = 0.12
elif sales > 10000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145

if commission == 0:
    print("error")
else:
    pay_out = commission * sales
    print(f"{pay_out:.2f}")