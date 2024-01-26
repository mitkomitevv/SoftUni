n = int(input())
matrix = []

bunny_pos = []
best_direction = None
best_path = []
max_eggs = float("-inf")

possible_moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for r in range(n):
    matrix.append(input().split())

    if 'B' in matrix[r]:
        bunny_pos = [r, matrix[r].index('B')]

for direction, position in possible_moves.items():
    row, col = bunny_pos[0] + position[0], bunny_pos[1] + position[1]

    path = []
    collected_eggs = 0

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'X':
            break

        path.append([row, col])
        collected_eggs += int(matrix[row][col])
        row += position[0]
        col += position[1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)
