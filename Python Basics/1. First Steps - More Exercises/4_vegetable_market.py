vegetable_price = float(input())
fruits_price = float(input())
vegetable_quantity = float(input())
fruits_quantity = float(input())

vegetables_income = vegetable_price * vegetable_quantity
fruits_income = fruits_price * fruits_quantity
total_in_eur = (vegetables_income + fruits_income) / 1.94

print(f"{total_in_eur:.2f}")