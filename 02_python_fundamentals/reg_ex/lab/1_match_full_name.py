import re

names = input()
names_pattern = r"\b[A-Z]{1}[a-z]{1,} [A-Z]{1}[a-z]{1,}\b"
valid_names = re.findall(names_pattern, names)
print(" ".join(valid_names))