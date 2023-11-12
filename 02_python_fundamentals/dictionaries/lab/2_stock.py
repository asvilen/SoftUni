food_storage = input().split()
food_stock_dict = {}
for index in range(0, len(food_storage), 2):
    key = food_storage[index]
    value = int(food_storage[index + 1])
    food_stock_dict[key] = value
food_to_search = input().split()
for food_type in food_to_search:
    if food_type in food_stock_dict:
        quantity = food_stock_dict[food_type]
        print(f"We have {quantity} of {food_type} left")
    else:
        print(f"Sorry, we don't have {food_type}")