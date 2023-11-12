resources_dictionary = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resources_dictionary:
        resources_dictionary[resource] = 0
    resources_dictionary[resource] += quantity

for resource in resources_dictionary:
    print(f"{resource} -> {resources_dictionary[resource]}")