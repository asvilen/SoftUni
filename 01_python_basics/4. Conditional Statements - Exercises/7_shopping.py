budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = 250
video_cards_expenses = video_cards * video_cards_price
processors_price = video_cards_expenses * 0.35
ram_memory_price = video_cards_expenses * 0.10

total_expenses = video_cards_expenses + processors * processors_price + ram_memory * ram_memory_price

if video_cards > processors:
    total_expenses *= 0.85

difference = abs(total_expenses - budget)

if budget >= total_expenses:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")