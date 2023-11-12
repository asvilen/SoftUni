groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
all_people = 0

for group in range (1, groups + 1):
    n_people = int(input())
    all_people += n_people

    if n_people < 6:
        musala += n_people
    elif n_people <= 12:
        monblan += n_people
    elif n_people <= 25:
        kilimanjaro += n_people
    elif n_people <= 40:
        k2 += n_people
    else:
        everest += n_people

musala_perc = musala / all_people * 100
print(f"{musala_perc:.2f}%")
monblan_perc = monblan / all_people * 100
print(f"{monblan_perc:.2f}%")
kilimanjaro_perc = kilimanjaro / all_people * 100
print(f"{kilimanjaro_perc:.2f}%")
k2_perc = k2 / all_people * 100
print(f"{k2_perc:.2f}%")
everest_perc = everest / all_people * 100
print(f"{everest_perc:.2f}%")