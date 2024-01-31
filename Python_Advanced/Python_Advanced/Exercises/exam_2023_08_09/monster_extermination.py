from collections import deque

monsters = deque(int(x) for x in input().split(','))
soldier_attacks = deque(int(y) for y in input().split(','))
killed_monsters = 0

while monsters and soldier_attacks:
    monster = monsters.popleft()
    attack = soldier_attacks.pop()

    if attack >= monster:
        killed_monsters += 1
        if soldier_attacks:
            soldier_attacks[-1] += attack - monster
        elif not soldier_attacks and attack - monster > 0:
            soldier_attacks.append(attack - monster)
    else:
        monsters.append(monster - attack)

if not monsters:
    print("All monsters have been killed!")
if not soldier_attacks:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
