def valid_move():
    if 0 <= r < n and 0 <= c < m:
        return True


n, m = [int(x) for x in input().split(',')]

matrix = []
position = []
cheese = 0

for row in range(n):
    matrix.append([el for el in input()])
    if 'M' in matrix[row]:
        position = [row, matrix[row].index('M')]
        matrix[position[0]][position[1]] = '*'
    cheese += matrix[row].count('C')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

direction = input()
while direction != 'danger':
    move_direction = directions[direction]
    r, c = position[0] + move_direction[0], position[1] + move_direction[1]

    if not valid_move():
        print("No more cheese for tonight!")
        break
    else:
        if matrix[r][c] == 'C':
            cheese -= 1
            if cheese == 0:
                position = [r, c]
                print("Happy mouse! All the cheese is eaten, good night!")
                break
            else:
                matrix[r][c] = '*'
        elif matrix[r][c] == 'T':
            position = [r, c]
            print("Mouse is trapped!")
            break
        elif matrix[r][c] == '@':
            direction = input()
            continue

        position = [r, c]

    direction = input()

if direction == 'danger':
    print("Mouse will come back later!")
matrix[position[0]][position[1]] = 'M'
[print(*row, sep='') for row in matrix]
