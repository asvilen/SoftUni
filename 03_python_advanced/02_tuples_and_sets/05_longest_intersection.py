n_of_lines = int(input())

longest_intersection = set()

for line in range(n_of_lines):
    first_set = set()
    second_set = set()
    first, second = input().split("-")

    first_start, first_end = int(first[:first.index(',')]), int(first[first.index(',') + 1:])
    second_start, second_end = int(second[:second.index(',')]), int(second[second.index(',') + 1:])
    for first_numbers in range(first_start, first_end + 1):
        first_set.add(first_numbers)
    for second_numbers in range(second_start, second_end + 1):
        second_set.add(second_numbers)
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f"Longest intersection is {[x for x in longest_intersection]} with length {len(longest_intersection)}")

# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11

# Longest intersection is [6, 7, 8, 9, 10] with length 5