exp_to_gain = int(input())
battle_count = int(input())
gained_exp = 0
gained_enough = False
for battle in range(1, battle_count + 1):
    current_battle_exp = int(input())
    if battle % 3 == 0:
        if battle % 5 == 0:
            current_battle_exp = current_battle_exp * 1.05
        else:
            current_battle_exp = current_battle_exp * 1.15
    elif battle % 5 == 0:
        current_battle_exp = current_battle_exp * 0.9
    gained_exp += current_battle_exp
    if gained_exp >= exp_to_gain:
        gained_enough = True
        break

if gained_enough:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    needed_exp = exp_to_gain - gained_exp
    print(f"Player was not able to collect the needed experience, {needed_exp:.2f} more needed.")