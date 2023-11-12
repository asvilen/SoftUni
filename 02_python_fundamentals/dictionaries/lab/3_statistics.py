received_input = input()
product_dictionary = {}
total_products = 0
total_quantity = 0
while received_input != 'statistics':
    pair = received_input.split(': ')
    key = pair[0]
    value = int(pair[1])
    if key not in product_dictionary:
        product_dictionary[key] = value
        total_products += 1

    else:
        product_dictionary[key] += value
    total_quantity += value
    received_input = input()
print("Products in stock:")
for product, quantity in product_dictionary.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
