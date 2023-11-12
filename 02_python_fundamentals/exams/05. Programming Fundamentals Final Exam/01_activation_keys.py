activation_key = input()

while True:
    command = input().split(">>>")
    if command[0] == 'Generate':
        break
    elif command[0] == 'Contains':
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
    elif command[0] == 'Flip':
        start_index, end_index = int(command[2]), int(command[3])
        before = activation_key[:start_index]
        after = activation_key[end_index:]
        to_flip = activation_key[start_index:end_index]
        if command[1] == 'Upper':
            activation_key = before + to_flip.upper() + after
        else: # command[1] == 'Lower'
            activation_key = before + to_flip.lower() + after
        print(activation_key)
    elif command[0] == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        before = activation_key[:start_index]
        after = activation_key[end_index:]
        activation_key = before + after
        print(activation_key)
print(f"Your activation key is: {activation_key}")
