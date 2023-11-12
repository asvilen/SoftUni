def even_odd_filter(**kwargs):
    resulting_dict = {}
    for key in kwargs:
        resulting_dict[key] = []
        if key == "odd":
            resulting_dict[key] = [x for x in kwargs[key] if x % 2 != 0]
        else:
            resulting_dict[key] = [x for x in kwargs[key] if x % 2 == 0]
    return dict(sorted(resulting_dict.items(), key=lambda item: (-len(item[1]))))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
