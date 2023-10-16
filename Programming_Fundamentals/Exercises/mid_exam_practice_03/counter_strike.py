energy = int(input())
won = 0
flag = False
while True:
    command = input()
    if command == 'End of battle':
        break
    distance = int(command)
    if energy - distance < 0:
        flag = True
        break
    won += 1
    energy -= distance
    if won % 3 == 0:
        energy += won
if flag:
    print(f'Not enough energy! Game ends with {won} won battles and {energy} energy')
else:
    print(f'Won battles: {won}. Energy left: {energy}')