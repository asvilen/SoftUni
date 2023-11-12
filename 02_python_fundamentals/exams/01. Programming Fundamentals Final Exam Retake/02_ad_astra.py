import re

input_expression = input()
pattern = r'(?P<symbol>[|#])(?P<item_name>\w*\s*\w+)\1(?P<expiration>[0-9]{2}(?P<f_slash>\/)[0-9]{2}\4[0-9]{2})\1(?P<calories>\d+)\1'

matches = re.finditer(pattern, input_expression)
items, calories, date = [], [], []
for match in matches:
    items.append(match.group('item_name'))
    date.append(match.group('expiration'))
    calories.append(int(match.group('calories')))


total_calories = sum(calories)
days_to_last = int(total_calories / 2000)
print(f"You have food to last you for: {days_to_last} days!")

for row in range(len(items)):
    print(f"Item: {items[row]}, Best before: {date[row]}, Nutrition: {calories[row]}")