SIZE = 6
matrix = []

for _ in range(SIZE):
    matrix.append(input().split())

position = input().strip('(').strip(')').split(', ')
r, c = int(position[0]), int(position[1])

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

input_line = input().split(', ')
while input_line[0] != 'Stop':
    command, direction = input_line[0], input_line[1]
    r, c = r + directions[direction][0],c + directions[direction][1]

    if command == 'Create':
        value = input_line[2]
        if matrix[r][c] == '.':
            matrix[r][c] = value

    elif command == 'Update':
        value = input_line[2]
        if matrix[r][c] != '.':
            matrix[r][c] = value

    elif command == 'Delete':
        if matrix[r][c] != '.':
            matrix[r][c] = '.'

    elif command == 'Read':
        if matrix[r][c] != '.':
            print(matrix[r][c])

    input_line = input().split(', ')

[print(*row) for row in matrix]
