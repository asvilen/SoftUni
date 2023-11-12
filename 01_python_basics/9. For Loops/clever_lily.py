age = int(input())
w_price = float(input())
t_price = int(input())

toys = 0
money = 10
m_sum = 0
b_stoll = 0

for year in range(1, age + 1):
    if year % 2 != 0:
        toys += 1
    else:
        m_sum += money
        money += 10
        b_stoll += 1

total = m_sum + (toys * t_price) - b_stoll
diff = abs(total - w_price)

if total >= w_price:
    print(f"Yes! {diff}")
else:
    print(f"No! {diff}")