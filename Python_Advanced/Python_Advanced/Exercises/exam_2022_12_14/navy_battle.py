n = int(input())

matrix = []
mines, battlecruisers = 3, 3
position = []

for row in range(n):
    matrix.append([x for x in input()])
    if 'S' in matrix[row]:
        position = [row, matrix[row].index('S')]
        matrix[position[0]][position[1]] = '-'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:
    direction = input()
    r, c = position[0] + directions[direction][0], position[1] + directions[direction][1]

    if matrix[r][c] == '*':
        mines -= 1
    elif matrix[r][c] == 'C':
        battlecruisers -= 1

    position = [r, c]
    matrix[r][c] = '-'

    if mines == 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
        break
    if battlecruisers == 0:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

matrix[position[0]][position[1]] = 'S'
[print(*row, sep='') for row in matrix]
