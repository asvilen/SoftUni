dwarfs_drawer = {}
while True:
    current_inputs = input()
    if current_inputs == "Once upon a time":
        break
    current_inputs = current_inputs.split(" <:> ")
    name, hat_color, physics = current_inputs[0], current_inputs[1], int(current_inputs[2])
    if name not in dwarfs_drawer:
        dwarfs_drawer[name] = {}
    if hat_color not in dwarfs_drawer[name]:
        dwarfs_drawer[name][hat_color] = physics
    else:
        dwarfs_drawer[name][hat_color] = max(dwarfs_drawer[name][hat_color], physics)

by_color = {}
for name in dwarfs_drawer.keys():
    for color in dwarfs_drawer[name]:
        if color not in by_color:
            by_color[color] = {}
        by_color[color][name] = dwarfs_drawer[name][color]

by_color = dict(sorted(by_color.items(), key=lambda x: (list(x[1].values()), len(x[1])), reverse=True))
for color in by_color:
    for name in by_color[color]:
        print(f"({color}) {name} <-> {by_color[color][name]}")

#
# Peter <:> Red <:> 2000
# Teodor <:> Blue <:> 1000
# George <:> Green <:> 1000
# Simon <:> Yellow <:> 4500
# Dopey <:> Simon <:> 1000
# Once upon a time
#
# Grumpy <:> Red <:> 5000
# Grumpy <:> Blue <:> 10000
# Grumpy <:> Red <:> 10000
# Happy <:> Blue <:> 10000
# Once upon a time
