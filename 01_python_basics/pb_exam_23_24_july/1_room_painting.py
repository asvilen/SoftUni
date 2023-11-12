from math import ceil, floor

broi_kutii = int(input())
broi_rolki = int(input())
cena_na_edin_chift_rykavici = float(input())
cena_na_edin_broi_chetka = float(input())

cena_kutiq_boia = 21.50
cena_na_rolka = 5.20
broi_rykavici = ceil(0.35 * broi_rolki)
broi_chetki = floor(0.48 * broi_kutii)

obshta_suma = broi_rykavici * cena_na_edin_chift_rykavici + \
              broi_chetki * cena_na_edin_broi_chetka + \
              broi_kutii * cena_kutiq_boia + \
              broi_rolki * cena_na_rolka
dostavka = obshta_suma / 15

print(f"This delivery will cost {dostavka:.2f} lv.")