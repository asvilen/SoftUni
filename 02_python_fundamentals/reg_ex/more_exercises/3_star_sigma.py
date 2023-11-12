import re

number_of_messages = int(input())
code_pattern = r"[S,s,T,t,A,a,R,r]"
encryption_pattern = r"@([A-Za-z]+)[^@!:>-]*:([0-9]+)[^@!:>-]*!([A,D])![^@!:>-]*->([0-9]+)"
attacked_planets = []
destroyed_planets = []
for message in range(number_of_messages):
    current_message = input()
    code_list = re.findall(code_pattern, current_message)
    current_code = len(code_list)
    current_encoding = []
    for letter in current_message:
        current_letter = chr(ord(letter) - current_code)
        current_encoding.append(current_letter)
    current_decrypted_message = "".join(current_encoding)
    decrypted_message_info = re.search(encryption_pattern, current_decrypted_message)
    if decrypted_message_info:
        planet, population, action, soldiers = decrypted_message_info.groups()
        if action == "A":
            attacked_planets.append(planet)
        elif action == "D":
            destroyed_planets.append(planet)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")