def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda item: (-len(item[1]), item[0]))
    final_string = ""
    for name, quantities in sorted_cheeses:
        final_string += f"{name}\n"
        for value in sorted(quantities, reverse=True):
            final_string += str(value) + "\n"
    return final_string



print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
