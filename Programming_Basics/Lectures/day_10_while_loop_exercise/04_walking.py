steps_counter = 0
goal = 10000
steps = input()
while steps != 'Going home':
    steps = int(steps)
    steps_counter += steps

    if steps_counter >= goal:
        break

    steps = input()

if steps == 'Going home':
    steps = int(input())
    steps_counter += steps

diff = abs(steps_counter - goal)
if steps_counter >= goal:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
