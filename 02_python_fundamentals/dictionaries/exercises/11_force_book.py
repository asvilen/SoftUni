force_sides = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        already_in = False
        command = command.split(" | ")
        force_side, force_user = command
        for force_users in force_sides.values():
            if force_user in force_users:
                already_in = True
                break
        if not already_in:
            if force_side not in force_sides.keys():
                force_sides[force_side] = [force_user]
            else:
                force_sides[force_side].append(force_user)
    else:
        command = command.split(" -> ")
        force_user, force_side = command
        for force_users in force_sides.values():
            if force_user in force_users:
                index_to_pop = force_users.index(force_user)
                change_sides = force_users.pop(index_to_pop)
                break
        if force_side not in force_sides.keys():
            force_sides[force_side] = [force_user]
        else:
            force_sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for side, users in force_sides.items():
    if len(force_sides[side]) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
