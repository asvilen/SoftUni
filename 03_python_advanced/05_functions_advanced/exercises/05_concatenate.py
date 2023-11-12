def concatenate(*args, **kwargs):
    resulting_string = "".join([string for string in args])
    for key in kwargs.keys():
        if key in resulting_string:
            resulting_string = resulting_string.replace(key, kwargs[key])
    return resulting_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))