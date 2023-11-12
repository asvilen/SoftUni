bag = {}
had_a_winner = False
while not had_a_winner:
    winnings = input().split()
    for cycle in range(0, len(winnings), 2):
        amount = int(winnings[cycle])
        item = winnings[cycle + 1].lower()
        if item not in bag:
            bag[item] = 0
        bag[item] += amount

        if "shards" in bag and bag["shards"] >= 250:
            had_a_winner = True
            bag["shards"] -= 250
            won_item = "Shadowmourne"
            break
        elif "fragments" in bag and bag["fragments"] >= 250:
            had_a_winner = True
            bag["fragments"] -= 250
            won_item = "Valanyr"
            break
        elif "motes" in bag and bag["motes"] >= 250:
            had_a_winner = True
            bag["motes"] -= 250
            won_item = "Dragonwrath"
            break

print(f"{won_item} obtained!")
for item in ["shards", "fragments", "motes"]:
    if item not in bag:
        bag[item] = 0
    print(f"{item}: {bag[item]}")
    bag.pop(item)
for item in bag:
    print(f"{item}: {bag[item]}")