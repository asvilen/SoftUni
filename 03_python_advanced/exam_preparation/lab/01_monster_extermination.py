from collections import deque

monster_armour = deque([int(x) for x in input().split(",")])
soldier_striking = [int(x) for x in input().split(",")]
killed_monsters = 0

while monster_armour and soldier_striking:
    current_monster = monster_armour.popleft()
    current_soldier = soldier_striking.pop()
    if current_soldier >= current_monster:
        killed_monsters += 1
        current_soldier -= current_monster
        if soldier_striking:
            soldier_striking[-1] += current_soldier
        elif current_soldier > 0:
            soldier_striking.append(current_soldier)
    else:
        current_monster -= current_soldier
        monster_armour.append(current_monster)
if not monster_armour:
    print("All monsters have been killed!")
if not soldier_striking:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
