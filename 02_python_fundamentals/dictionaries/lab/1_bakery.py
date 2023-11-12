food_storage = input().split()
food_dictionary = {}
for index in range(0, len(food_storage), 2):
    key = food_storage[index]
    value = int(food_storage[index + 1])
    food_dictionary[key] = value
print(food_dictionary)
