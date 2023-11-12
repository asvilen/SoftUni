n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1, n + 1):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif current_number <= 399:
        p2 += 1
    elif current_number <= 599:
        p3 += 1
    elif current_number <= 799:
        p4 += 1
    else:
        p5 += 1

p1_perc = p1 / n * 100
print(f"Under 200: {p1_perc:.2f}%")
p2_perc = p2 / n * 100
print(f"between 200 and 399: {p2_perc:.2f}%")
p3_perc = p3 / n * 100
print(f"between 400 and 599: {p3_perc:.2f}%")
p4_perc = p4 / n * 100
print(f"between 600 and 799: {p4_perc:.2f}%")
p5_perc = p5 / n * 100
print(f"over 800: {p5_perc:.2f}%")
