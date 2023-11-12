cat_type = input()
sex = input()

valid_type = True
years = 0

if sex == "m":
    if cat_type == "British Shorthair":
        years = 13
    elif cat_type == "Siamese":
        years = 15
    elif cat_type == "Persian":
        years = 14
    elif cat_type == "Ragdoll":
        years = 16
    elif cat_type == "American Shorthair":
        years = 12
    elif cat_type == "Siberian":
        years = 11
    else:
        valid_type = False
elif sex == "f":
    if cat_type == "British Shorthair":
        years = 14
    elif cat_type == "Siamese":
        years = 16
    elif cat_type == "Persian":
        years = 15
    elif cat_type == "Ragdoll":
        years = 17
    elif cat_type == "American Shorthair":
        years = 13
    elif cat_type == "Siberian":
        years = 12
    else:
        valid_type = False

cat_months = years * 2
if valid_type:
    print(f"{int(cat_months)} cat months")
else:
    print(f"{cat_type} is invalid cat!")