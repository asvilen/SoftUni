n = int(input())
m = int(input())
s = int(input())

for adres in range(m, n - 1, -1):
    if adres % 2 == 0 and adres % 3 == 0:
        if adres == s:
            break
        else:
            print(adres, end = " ")