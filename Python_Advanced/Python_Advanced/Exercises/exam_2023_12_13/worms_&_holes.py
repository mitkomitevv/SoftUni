from collections import deque

worms = deque(int(x) for x in input().split())
holes = deque(int(x) for x in input().split())
matches, unmatched_worms = 0, 0


while worms and holes:
    worm, hole = worms.pop(), holes.popleft()

    if worm == hole:
        matches += 1
    else:
        worm -= 3
        if worm > 0:
            worms.append(worm)
        else:
            unmatched_worms += 1

print(f"Matches: {matches}" if matches > 0 else "There are no matches.")
if worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
elif unmatched_worms > 0:
    print("Worms left: none")
else:
    print("Every worm found a suitable hole!")
print(f"Holes left: {', '.join(str(x) for x in holes)}" if holes else "Holes left: none")
