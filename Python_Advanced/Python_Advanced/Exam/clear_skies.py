n = int(input())

matrix = []
position = []
armor, enemy_jets = 300, 0

for row in range(n):
    matrix.append([x for x in input()])
    if 'J' in matrix[row]:
        position = [row, matrix[row].index('J')]
        matrix[row][matrix[row].index('J')] = '-'
    if 'E' in matrix[row]:
        enemy_jets += sum(1 for el in matrix[row] if el == 'E')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

direction = input()
while True:
    r, c = position[0] + directions[direction][0], position[1] + directions[direction][1]

    if matrix[r][c] == 'E':
        if enemy_jets > 1:
            armor -= 100
        enemy_jets -= 1
    elif matrix[r][c] == 'R':
        armor = 300

    position = [r, c]
    matrix[r][c] = '-'

    if enemy_jets == 0:
        break
    if armor == 0:
        break

    direction = input()

matrix[position[0]][position[1]] = 'J'
if not enemy_jets:
    print("Mission accomplished, you neutralized the aerial threat!")
else:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}]!")
[print(''.join(row)) for row in matrix]
