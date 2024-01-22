from copy import deepcopy

def bunny_move(matrix_move, matrix_copy):
    for row1 in range(rows):
        for col1 in range(cols):
            if matrix_copy[row1][col1] == 'B':
                for x, y in directions.values():
                    b_r, b_c = row1 + x, col1 + y

                    if 0 <= b_r < rows and 0 <= b_c < cols:
                        matrix_move[b_r][b_c] = 'B'
    return matrix_move

rows, cols = [int(n) for n in input().split()]
matrix = [[el for el in input()] for _ in range(rows)]
moves = input()

copy_matrix = deepcopy(matrix)
position = []

directions = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0],
}
player_found = False
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'P':
            position = [row, col]
            matrix[row][col] = '.'
            player_found = True
            break
    if player_found:
        break

for move in moves:
    move_direction = directions[move]
    r, c = position[0] + move_direction[0], position[1] + move_direction[1]

    if 0 <= r < rows and 0 <= c < cols:
        position = [r, c]
        if matrix[r][c] == 'B':
            matrix = bunny_move(matrix, copy_matrix)
            copy_matrix = deepcopy(matrix)
            [print(*row, sep='') for row in matrix]
            print(f"dead: {r} {c}")
            break

        matrix = bunny_move(matrix, copy_matrix)
        copy_matrix = deepcopy(matrix)

        if matrix[r][c] == 'B':
            [print(*row, sep='') for row in matrix]
            print(f"dead: {r} {c}")
            break

    else:
        matrix = bunny_move(matrix, copy_matrix)
        [print(*row, sep='') for row in matrix]
        print(f"won: {r - move_direction[0]} {c - move_direction[1]}")
        break
