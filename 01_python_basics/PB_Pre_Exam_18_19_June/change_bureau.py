bitcoin_amount = int(input())
yuan_amount = float(input())
commission = float(input())

btc_bgn = 1168
cny_usd = 0.15
usd_bgn = 1.76
eur_bgn = 1.95
btc_eur = btc_bgn / eur_bgn
cny_eur = cny_usd * usd_bgn / eur_bgn

total_eur = (bitcoin_amount * btc_eur + yuan_amount * cny_eur) * (100 - commission) / 100
print(f"{total_eur:.2f}")