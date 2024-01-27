n = int(input())

matrix = []
alice_pos = []
tea_collected = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(n):
    matrix.append([int(el) if el.isdigit() else el for el in input().split()])
    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[row][alice_pos[1]] = '.'

command = input()
while tea_collected < 10:

    matrix[alice_pos[0]][alice_pos[1]] = '*'
    move_direction = directions[command]
    r, c = alice_pos[0] + move_direction[0], alice_pos[1] + move_direction[1]

    if 0 <= r < n and 0 <= c < n:
        alice_pos = [r, c]
        if isinstance(matrix[r][c], int):
            tea_collected += matrix[r][c]
        if tea_collected >= 10:
            matrix[alice_pos[0]][alice_pos[1]] = '*'
            print("She did it! She went to the party.")
            break
        elif matrix[r][c] == 'R':
            matrix[alice_pos[0]][alice_pos[1]] = '*'
            print("Alice didn't make it to the tea party.")
            break
    else:

        print("Alice didn't make it to the tea party.")
        break

    command = input()
[print(*row) for row in matrix]
