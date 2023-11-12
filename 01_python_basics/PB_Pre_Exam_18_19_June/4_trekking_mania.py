groups_count = int(input())

people_count = 0
peak_m = 0
peak_mon = 0
peak_ki = 0
peak_k2 = 0
peak_everest = 0

for group in range(groups_count):
    people = int(input())
    people_count += people
    if people <= 5:
        peak_m += people
    elif people <= 12:
        peak_mon += people
    elif people <= 25:
        peak_ki += people
    elif people <= 40:
        peak_k2 += people
    elif people > 40:
        peak_everest += people

per_m = peak_m / people_count * 100
per_mon = peak_mon / people_count * 100
per_ki = peak_ki / people_count * 100
per_k2 = peak_k2 / people_count * 100
per_everest = peak_everest / people_count * 100

print(f"{per_m:.2f}%")
print(f"{per_mon:.2f}%")
print(f"{per_ki:.2f}%")
print(f"{per_k2:.2f}%")
print(f"{per_everest:.2f}%")