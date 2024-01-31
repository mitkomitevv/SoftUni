def valid_move():
    if 0 <= r < n and 0 <= c < m:
        return True


n, m = [int(x) for x in input().split()]
matrix  = []
position = [0, 0]
out_of_bounds = False

for row in range(n):
    matrix.append([el for el in input()])
    if 'B' in matrix[row]:
        position = [row, matrix[row].index('B')]
        matrix[position[0]][position[1]] = '.'

starting_position = position

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}


while True:
    direction = input()
    move_direction = directions[direction]
    r, c = position[0] + move_direction[0], position[1] + move_direction[1]

    if not valid_move():
        print("The delivery is late. Order is canceled.")
        out_of_bounds = True
        break
    else:
        if matrix[r][c] == '-':
            matrix[r][c] = '.'
        if matrix[r][c] == 'P':
            matrix[r][c] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")
        elif matrix[r][c] == '*':
            continue
        elif matrix[r][c] == 'A':
            matrix[r][c] = 'P'
            print("Pizza is delivered on time! Next order...")
            break

        position = [r, c]

matrix[starting_position[0]][starting_position[1]] = 'B' if not out_of_bounds else ' '
[print(''.join(row)) for row in matrix]
