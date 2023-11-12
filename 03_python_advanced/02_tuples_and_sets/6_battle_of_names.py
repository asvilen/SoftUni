received_number = int(input())
odd_set = set()
even_set = set()
for name in range(1, received_number + 1):
    current_name = input()
    current_ascii_sum = sum([ord(value) for value in current_name])
    current_result = int(current_ascii_sum / name)
    if current_result % 2 == 0:
        even_set.add(current_result)
    else:
        odd_set.add(current_result)
odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    to_print = odd_set.union(even_set)
elif odd_sum > even_sum:
    to_print = odd_set.difference(even_set)
elif odd_sum < even_sum:
    to_print = odd_set.symmetric_difference(even_set)
print(*to_print, sep=", ")

# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan