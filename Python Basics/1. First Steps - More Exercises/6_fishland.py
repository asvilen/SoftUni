macherel_price = float(input())
sprat_price = float(input())
bonito_amount = float(input())
scad_amount = float(input())
clam_amount = int(input())

bonito_price = macherel_price * 1.6
scad_price = sprat_price * 1.8
clam_price = 7.5

total_bill = bonito_price * bonito_amount + scad_amount * scad_price + clam_price * clam_amount

print(f"{total_bill:.2f}")