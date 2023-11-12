import re

dates = input()
date_pattern = r"\b\d{2}[.]\w{3}[.]\d{4}\b|\b\d{2}[-]\w{3}[-]\d{4}\b|\b\d{2}[/]\w{3}[/]\d{4}\b"
date_pattern_2 = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"

all_dates = re.findall(date_pattern_2, dates)

for match in all_dates:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
