presents_count = int(input())
size = int(input())
matrix = []
nice_kids = 0
happy_kids = 0
santa_position = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(size):
    matrix.append([el for el in input().split()])
    if 'S' in matrix[row]:
        santa_position = [row, matrix[row].index('S')]
        matrix[santa_position[0]][santa_position[1]] = '-'
    nice_kids += matrix[row].count('V')

direction = input()
while direction != 'Christmas morning':
    move_direction = directions[direction]
    r, c = santa_position[0] + move_direction[0], santa_position[1] + move_direction[1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == 'X':
            matrix[r][c] = '-'

        elif matrix[r][c] == 'V':
            matrix[r][c] = '-'
            presents_count -= 1
            happy_kids += 1

        elif matrix[r][c] == 'C':
            for value in directions.values():
                row, col = r + value[0], c + value[1]
                if 0 <= row < size and 0 <= col < size:
                    if matrix[row][col] == 'X':
                        matrix[row][col] = '-'
                        presents_count -= 1

                    elif matrix[row][col] == 'V':
                        matrix[row][col] = '-'
                        presents_count -= 1
                        happy_kids += 1
        santa_position = [r, c]
    if presents_count == 0:
        break
    direction = input()

matrix[santa_position[0]][santa_position[1]] = 'S'
if presents_count == 0 and happy_kids < nice_kids:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if happy_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - happy_kids} nice kid/s.")
