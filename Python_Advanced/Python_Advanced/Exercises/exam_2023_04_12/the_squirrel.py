def valid_move():
    if 0 <= r < n and 0 <= c < n:
        return True


n = int(input())
moves = input().split(', ')

matrix = []
position = []
hazelnuts = 0
out_of_bounds, trap = False, False

for row in range(n):
    matrix.append([el for el in input()])
    if 's' in matrix[row]:
        position = [row, matrix[row].index('s')]
        matrix[position[0]][position[1]] = '*'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for move in moves:
    direction = directions[move]
    r, c = position[0] + direction[0], position[1] + direction[1]

    if not valid_move():
        print("The squirrel is out of the field.")
        out_of_bounds = True
        break
    else:
        if matrix[r][c] == 'h':
            matrix[r][c] = '*'
            hazelnuts += 1
            if hazelnuts == 3:
                break
        elif matrix[r][c] == 't':
            trap = True
            print("Unfortunately, the squirrel stepped on a trap...")
            break

    position = [r, c]

if hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")
elif not out_of_bounds and not trap:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
