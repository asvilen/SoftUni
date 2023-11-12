numbers_list = input().split("|")
m_stack = []
for row in numbers_list:
    current_row = [int(x) for x in row.split()]
    if current_row:
        m_stack.append(current_row)
while m_stack:
    print(*m_stack.pop(), sep=' ', end=' ')