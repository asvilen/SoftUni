def accommodate_new_pets(capacity: int, max_weight: float, *args):
    accommodated_pets = 0
    pets_dict = {}
    success = True
    for pet, pet_weight in args:
        if capacity > accommodated_pets:
            if max_weight >= pet_weight:
                accommodated_pets += 1
                if pet not in pets_dict:
                    pets_dict[pet] = 0
                pets_dict[pet] += 1
        else:
            success = False
            break
    message = ""
    available_capacity = capacity - accommodated_pets
    if success:
        message += f"All pets are accommodated! Available capacity: {available_capacity}.\n"
    else:
        message += "You did not manage to accommodate all pets!\n"
    message += "Accommodated pets:\n"
    for pet_type, amount in sorted(pets_dict.items(), key=lambda item: item[0]):
        message += f"{pet_type}: {amount}\n"
    return message


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
