from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while True:
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
    if not tools or not substances:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance
    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(tool + 1)
        if substance > 1:
            substances.append(substance - 1)

if tools:
    print("Tools:", end=" ")
    print(*tools, sep=", ")
if substances:
    print("Substances:", end=" ")
    print(*substances, sep=", ")
if challenges:
    print("Challenges:", end=" ")
    print(*challenges, sep=", ")
