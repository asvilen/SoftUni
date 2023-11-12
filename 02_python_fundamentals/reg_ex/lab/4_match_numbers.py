import re

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
text = input()

valid_numbers = re.finditer(pattern, text)
valid_numbers = [number.group() for number in valid_numbers]
print(" ".join(valid_numbers))