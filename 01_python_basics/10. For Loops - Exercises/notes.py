n = int(input())


for position in range(1, n + 1):
    if position % 2 == 0:
        print(f"{position} is even")
    else:
        print(f"{position} is odd")