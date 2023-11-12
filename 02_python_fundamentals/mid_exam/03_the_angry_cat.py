price_ratings_string = input()
price_ratings_list = [int(price) for price in price_ratings_string.split(", ")]
point_of_entry = int(input())
type_of_item = input()

entry_item_price = price_ratings_list[point_of_entry]


def broken_sum_calc(item_type, entry_price, items):
    if item_type == "cheap":
        return sum([item for item in items if item < entry_price])
    else:
        return sum([item for item in items if item >= entry_price])


left_sum = broken_sum_calc(type_of_item, entry_item_price, price_ratings_list[:point_of_entry])
right_sum = broken_sum_calc(type_of_item, entry_item_price, price_ratings_list[point_of_entry + 1:])

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")
