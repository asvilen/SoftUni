size = int(input())

primary = []
secondary = []

for index in range(size):
    current_row = [int(x) for x in input().split(", ")]
    primary.append(current_row[index])
    secondary.append(current_row[-index - 1])

print("Primary diagonal: ", end="")
print(*primary, sep=", ", end=". ")
print(f"Sum: {sum(primary)}")

print("Secondary diagonal: ", end="")
print(*secondary, sep=", ", end=". ")
print(f"Sum: {sum(secondary)}")
