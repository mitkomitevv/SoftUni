matrix = []
count_targets = 0
targets_hit = []
position = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(5):
    matrix.append([el for el in input().split()])
    count_targets += matrix[row].count('x')
    if 'A' in matrix[row]:
        position = [row, matrix[row].index('A')]

for _ in range(int(input())):
    data = input().split()
    command, direction = data[0], data[1]
    matrix[position[0]][position[1]] = '.'
    move_direction = directions[direction]

    if command == 'move':
        n = int(data[2])
        r, c = position[0] + (move_direction[0] * n), position[1] + (move_direction[1]) * n
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == '.':
                position = [r , c]

    elif command == 'shoot':
        shoot_direction = move_direction
        for i in range(len(matrix)):
            r, c = position[0] + (shoot_direction[0] * i), position[1] + (shoot_direction[1]) * i
            if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == 'x':
                    matrix[r][c] = '.'
                    count_targets -= 1
                    targets_hit.append([r, c])
                    break
    if count_targets == 0:
        break

if count_targets == 0:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {count_targets} targets left.")
[print(row, sep='\n') for row in targets_hit]
