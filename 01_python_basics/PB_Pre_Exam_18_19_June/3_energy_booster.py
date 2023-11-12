fruit = input()
set_size = input()
sets_amount = int(input())

price_per_set = 0

if set_size == "small":
    if fruit == "Watermelon":
        price_per_set = 56 * 2
    elif fruit == "Mango":
        price_per_set = 36.66 * 2
    elif fruit == "Pineapple":
        price_per_set = 42.1 * 2
    elif fruit == "Raspberry":
        price_per_set = 20 * 2
elif set_size == "big":
    if fruit == "Watermelon":
        price_per_set = 28.7 * 5
    elif fruit == "Mango":
        price_per_set = 19.6 * 5
    elif fruit == "Pineapple":
        price_per_set = 24.8 * 5
    elif fruit == "Raspberry":
        price_per_set = 15.2 * 5

total_sum = sets_amount * price_per_set

if 400 <= total_sum <= 1000:
    total_sum *= 0.85
elif total_sum > 1000:
    total_sum *= 0.5

print(f"{total_sum:.2f} lv.")