word_1, word_2 = input().split()
total = 0
count = 0
for word_1_char, word_2_char in zip(word_1, word_2):
    count += 1
    total += ord(word_1_char) * ord(word_2_char)
left_over = ""
if len(word_1) > count:
    left_over = word_1[count:]
elif len(word_2) > count:
    left_over = word_2[count:]
total += sum([ord(char) for char in left_over])

print(total)