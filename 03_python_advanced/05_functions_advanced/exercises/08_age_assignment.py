def age_assignment(*args, **kwargs):
    result = []
    sorted_names = sorted(args)
    for name in sorted_names:
        for letter in kwargs:
            if name.startswith(letter):
                result.append(f"{name} is {kwargs[letter]} years old.")
                break
    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))