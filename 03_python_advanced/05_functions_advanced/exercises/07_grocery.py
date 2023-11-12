def grocery_store(**kwargs):
    result_list = []
    sorted_groceries_dict = dict(sorted(kwargs.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))
    for key, value in sorted_groceries_dict.items():
        result_list.append(f"{key}: {value}")
    return "\n".join(result_list)


print(grocery_store(
    eggs=12,
    bread=5,
    pasta=12,
))
print()
print(grocery_store(
    pasta=2,
    eggs=20,
    bread=2,
    carrot=1,
))
