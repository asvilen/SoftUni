n_numbers, m_numbers = [int(x) for x in input().split()]
n_set = set()
m_set = set()

for n in range(n_numbers):
    n_set.add(int(input()))
for m in range(m_numbers):
    m_set.add(int(input()))

print(*n_set.intersection(m_set), sep="\n")
# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5