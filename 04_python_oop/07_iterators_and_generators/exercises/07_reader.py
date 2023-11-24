def read_next(*args):
    for i in range(len(args)):
        for element in args[i]:
            yield element


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

print("===" * 10)

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')