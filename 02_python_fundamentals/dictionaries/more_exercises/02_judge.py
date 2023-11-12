contests_dict = {}
total_points_dict = {}
while True:
    current_input = input()
    if current_input == "no more time":
        break
    current_input_split = current_input.split(" -> ")
    username, contest, points = current_input_split[0], current_input_split[1], int(current_input_split[2])
    total_points_dict[username] = 0
    if contest not in contests_dict:
        contests_dict[contest] = {}
    if username in contests_dict[contest]:
        contests_dict[contest][username] = max(contests_dict[contest][username], points)
    else:
        contests_dict[contest][username] = points

for contest in contests_dict.keys():
    for user in contests_dict[contest].keys():
        total_points_dict[user] += contests_dict[contest][user]

for contest in contests_dict.keys():
    print(f"{contest}: {len(contests_dict[contest])} participants")
    ordered_contest_dict = dict(sorted(contests_dict[contest].items(), key=lambda x: (-x[1], x[0])))
    position = 1
    for user in ordered_contest_dict:
        print(f"{position}. {user} <::> {ordered_contest_dict[user]}")
        position += 1
print("Individual standings:")
position = 1
sorted_totals = dict(sorted(total_points_dict.items(), key=lambda x: (-x[1], x[0])))
for user in sorted_totals.keys():
    print(f"{position}. {user} -> {sorted_totals[user]}")
    position += 1

# Peter -> Algo -> 400
# George -> Algo -> 300
# Simo -> Algo -> 200
# Peter -> DS -> 150
# Mariya -> DS -> 600
# no more time
