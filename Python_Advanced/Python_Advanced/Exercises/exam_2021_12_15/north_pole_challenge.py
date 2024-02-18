rows, cols = [int(x) for x in input().split(', ')]
decorations = {'D': 0, 'G': 0, 'C': 0}
matrix = []
position = []
all_decor, collected, collected_everything = 0, 0, False

for row in range(rows):
    matrix.append(input().split())
    if 'Y' in matrix[row]:
        position = [row, matrix[row].index('Y')]
        matrix[row][matrix[row].index('Y')] = 'x'
    all_decor += sum(1 for item in matrix[row] if item not in ['.', 'x'])

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

command = input()
while command != 'End' and collected < all_decor:
    direction, steps = command.split('-')
    steps = int(steps)

    for _ in range(steps):
        r, c = (position[0] + directions[direction][0]) % rows, (position[1] + directions[direction][1]) % cols

        if matrix[r][c] != '.' and matrix[r][c] != 'x':
            decorations[matrix[r][c]] += 1
            collected += 1

        position = [r, c]
        matrix[r][c] = 'x'

        if collected == all_decor:
            collected_everything = True
            break

    if collected_everything:
        break

    command = input()

matrix[position[0]][position[1]] = 'Y'
if collected_everything:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations['D']} Christmas decorations")
print(f"- {decorations['G']} Gifts")
print(f"- {decorations['C']} Cookies")
[print(*row) for row in matrix]
