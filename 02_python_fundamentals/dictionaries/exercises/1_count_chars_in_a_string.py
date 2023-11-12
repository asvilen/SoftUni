string_input = input()
characters_dictionary = {}
for character in string_input:
    if character == " ":
        continue
    if character not in characters_dictionary:
        characters_dictionary[character] = 0
    characters_dictionary[character] += 1

for character in characters_dictionary:
    print(f"{character} -> {characters_dictionary[character]}")