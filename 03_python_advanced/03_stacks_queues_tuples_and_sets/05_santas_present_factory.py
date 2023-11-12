from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

manufactured_toys = []
magic_map = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_level:
    total_magic_level = materials[-1] * magic_level[0]

    if total_magic_level in magic_map.keys():
        magic_points = materials.pop() * magic_level.popleft()
        current_toy = magic_map[magic_points]
        manufactured_toys.append(current_toy)
    elif total_magic_level < 0:
        sum_of_values = materials.pop() + magic_level.popleft()
        materials.append(sum_of_values)
    elif total_magic_level > 0:
        magic_level.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic_level[0] == 0:
        materials.pop()
        magic_level.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic_level[0] == 0:
        magic_level.popleft()

if ("Doll" in manufactured_toys and "Wooden train" in manufactured_toys) \
        or ("Teddy bear" in manufactured_toys and "Bicycle" in manufactured_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left: ", end="")
    materials_reversed = []
    for _ in range(len(materials)):
        materials_reversed.append(materials.pop())
    print(*materials_reversed, sep=", ")
if magic_level:
    print("Magic left: ", end="")
    print(*magic_level, sep=", ")

for toy in sorted(set(manufactured_toys)):
    print(f"{toy}: {manufactured_toys.count(toy)}")

