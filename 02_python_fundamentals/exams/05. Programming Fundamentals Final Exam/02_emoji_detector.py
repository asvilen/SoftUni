import re

text_input = """
In the Sofia Zoo there are 311 animals in total! 
::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 
12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different 
types of :Snak::Es::. ::Mooning:: **Shy**
"""

colon_pattern = r"::([A-Z]{1}[a-z]{2,})::"
asterics_pattern = r"\*\*([A-Z]{1}[a-z]{2,})\*\*"

colon_matches = re.findall(colon_pattern, text_input)
asterics_matches = re.findall(asterics_pattern, text_input)

total_coolness = 0
for match in colon_matches:
    print(match)
    match_coolness = 0
    for letter in match:
        match_coolness += ord(letter)
    print(f"match_coolness: {match_coolness}")
for match in asterics_matches:
    print(match)
    match_coolness = 0
    for letter in match:
        match_coolness += ord(letter)
    print(f"match_coolness: {match_coolness}")
print(total_coolness)
