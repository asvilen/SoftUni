rows = int(input())
values_list = []
for row in range(rows):
    [values_list.append(int(x)) for x in input().split(", ")]
print(values_list)
