n = int(input())
matrix = []
position = []
fish = 0

for row in range(n):
    matrix.append([el for el in input()])
    if 'S' in matrix[row]:
        position = [row, matrix[row].index('S')]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

direction = input()
while direction != 'collect the nets':
    matrix[position[0]][position[1]] = '-'
    move_direction = directions[direction]
    r, c = (position[0] + move_direction[0]) % n, (position[1] + move_direction[1]) % n

    if matrix[r][c].isdigit():
        fish += int(matrix[r][c])
        matrix[r][c] = '-'
    elif matrix[r][c] == 'W':
        position = [r, c]
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{','.join(str(x) for x in position)}]")
        exit()

    position = [r, c]

    direction = input()

matrix[position[0]][position[1]] = 'S'
if fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish} tons of fish more.")
if fish > 0:
    print(f"Amount of fish caught: {fish} tons.")
[print(''.join(row)) for row in matrix]
