import re

phones = input()
phone_pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}"
valid_phones = re.findall(phone_pattern, phones)
print(", ".join(valid_phones))