from collections import deque

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

colors_string = deque(input().split())
found_colors = []

while colors_string:
    left = colors_string.popleft()
    right = colors_string.pop() if colors_string else ''
    substring = left + right
    substring_reversed = right + left
    if substring in main_colors or substring in secondary_colors.keys():
        found_colors.append(substring)
    elif substring_reversed in main_colors or substring_reversed in secondary_colors.keys():
        found_colors.append(substring_reversed)
    else:
        if len(left) > 1:
            colors_string.insert(len(colors_string) // 2, left[:-1])
        if len(right) > 1:
            colors_string.insert(len(colors_string) // 2, right[:-1])

for color in found_colors:
    if color in secondary_colors.keys():
        if not set(found_colors).issuperset(secondary_colors[color]):
            found_colors.remove(color)

print(found_colors)
