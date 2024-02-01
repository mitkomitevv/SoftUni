from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    tool, substance = tools.popleft(), substances.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(tool + 1)
        if substance - 1 > 0:
            substances.append(substance - 1)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
