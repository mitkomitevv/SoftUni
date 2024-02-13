SIZE = 6
matrix = []
position = [0, 0]
deposits = ['Water', 'Metal', 'Concrete']
found = set()

for row in range(SIZE):
    matrix.append([x for x in input().split()])
    if 'E' in matrix[row]:
        position = [row, matrix[row].index('E')]
        matrix[position[0]][position[1]] = '-'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

commands = input().split(', ')

for direction in commands:
    r, c = (position[0] + directions[direction][0]) % SIZE, (position[1] + directions[direction][1]) % SIZE

    if matrix[r][c] == 'R':
        print(f"Rover got broken at ({r}, {c})")
        break
    elif matrix[r][c] != '-':
        found.add(matrix[r][c])
        for deposit in deposits:
            if deposit.startswith(matrix[r][c]):
                print(f"{deposit} deposit found at ({r}, {c})")
                break

    position = [r, c]

print("Area suitable to start the colony." if len(found) == 3 else "Area not suitable to start the colony.")
