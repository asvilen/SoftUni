text = input()

lexicograph = {}

for character in text:
    if character not in lexicograph:
        lexicograph[character] = 1
    else:
        lexicograph[character] += 1

for char, count in sorted(lexicograph.items()):
    print(f"{char}: {count} time/s")

# Why do you like Python?