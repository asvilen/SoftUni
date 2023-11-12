import re
text_list = []
number_pattern = r"\d+"
while True:
    current_line = input()
    if current_line:
        text_list.append(current_line)
    else:
        break
one_line = "\n".join(text_list)
# print(one_line)
result = re.findall(number_pattern, one_line)
print(" ".join(result))