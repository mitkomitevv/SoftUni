def valid_move():
    if 0 <= r < n and 0 <= c < m:
        return True

n, m = [int(x) for x in input().split()]

matrix = []
position = []
touched_opponents, moves = 0, 0

for row in range(n):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        position = [row, matrix[row].index('B')]
        matrix[position[0]][position[1]] = '-'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

direction = input()
while direction != 'Finish' and touched_opponents < 3:
    move_direction = directions[direction]
    r, c = move_direction[0] + position[0], move_direction[1] + position[1]

    if valid_move():
        if matrix[r][c] == "P":
            position = [r, c]
            touched_opponents += 1
            moves += 1
            matrix[r][c] = '-'
        elif matrix[r][c] == '-':
            position = [r, c]
            moves += 1

    direction = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
