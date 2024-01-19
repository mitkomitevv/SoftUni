from collections import deque

cups = deque(int(c) for c in input().split())
bottles = deque(int(b) for b in input().split())
water_wasted = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()

    if bottle >= cup:
        water_wasted += bottle - cup
    elif bottle < cup:
        cup -= bottle
        cups.appendleft(cup)

bottles.reverse()
if bottles:
    print(f"Bottles:", *bottles)
else:
    print(f"Cups:", *cups)

print(f"Wasted litters of water: {water_wasted}")
