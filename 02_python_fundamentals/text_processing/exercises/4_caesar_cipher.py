word_to_encrypt = input()
encrypted_word = ""
for character in word_to_encrypt:
    ascii_position = ord(character) + 3
    encrypted_word += chr(ascii_position)
print(encrypted_word)