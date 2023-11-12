shirochina = float(input())
dyljina = float(input())
visochina = float(input())
sredna_visochina_na_anstronavtite = float(input())


obem_karyb = shirochina * dyljina * visochina
obem_staq_za_edin_astronavt = 2 * 2 * (sredna_visochina_na_anstronavtite + 0.40)
broi_astronavti = obem_karyb / obem_staq_za_edin_astronavt

#•	Ако броят на астронавтите е между 3 (вкл.) и 10 (вкл.):
if broi_astronavti >= 3 and broi_astronavti <= 10:
    print(f"The spacecraft holds {int(broi_astronavti)} astronauts.")
#•	Ако  броят на астронавтите е по-малък от 3:
elif broi_astronavti < 3:
    print("The spacecraft is too small.")
#•	Ако  броят на астронавтите е по-голям от 10:
elif broi_astronavti > 10:
    print("The spacecraft is too big.")