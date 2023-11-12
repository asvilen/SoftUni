count = int(input())

compounds = set()

for line in range(count):
    current_line_chemicals = input().split()
    for element in current_line_chemicals:
        compounds.add(element)
print(*compounds, sep="\n")
# 3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne