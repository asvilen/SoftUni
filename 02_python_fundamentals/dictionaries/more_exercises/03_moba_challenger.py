players_pool = {}
total_skills_dict = {}
while True:
    current_inputs = input()
    if current_inputs == "Season end":
        break
    if "->" in current_inputs:  # Add player/skill
        current_inputs = current_inputs.split(" -> ")
        player, position, skill = current_inputs[0], current_inputs[1], int(current_inputs[2])
        if player not in players_pool:
            players_pool[player] = {}
            total_skills_dict[player] = 0
        if position in players_pool[player]:
            players_pool[player][position] = max(players_pool[player][position], skill)
        else:
            players_pool[player][position] = skill
    else:  # Fight
        current_inputs = current_inputs.split(" vs ")
        player_1, player_2 = current_inputs[0], current_inputs[1]
        if player_1 in players_pool \
                and player_2 in players_pool:
            for position in players_pool[player_1]:
                if position in players_pool[player_2]:
                    if players_pool[player_1][position] > players_pool[player_2][position]:
                        del players_pool[player_2]
                        del total_skills_dict[player_2]
                        break
                    elif players_pool[player_1][position] < players_pool[player_2][position]:
                        del players_pool[player_1]
                        del total_skills_dict[player_1]
                        break

for player in players_pool.keys():
    for skill_points in players_pool[player].values():
        total_skills_dict[player] += skill_points

total_skills_dict = dict(sorted(total_skills_dict.items(), key=lambda x: (-x[1], x[0])))

for player in total_skills_dict:
    print(f"{player}: {total_skills_dict[player]} skill")
    ordered_skills = dict(sorted(players_pool[player].items(), key=lambda x: (-x[1], x[0])))
    for position in ordered_skills.keys():
        print(f"- {position} <::> {ordered_skills[position]}")

# Peter -> Adc -> 400
# George -> Jungle -> 300
# Simon -> Mid -> 200
# Simon -> Support -> 250
# Season end

# Peter -> Adc -> 400
# Bush -> Tank -> 150
# Frank -> Mid -> 200
# Frank -> Support -> 250
# Frank -> Tank -> 250
# Peter vs Frank
# Frank vs Bush
# Frank vs Hide
# Season end
