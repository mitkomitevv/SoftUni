def valid_coordinates():
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False

matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]

while True:
    command, *data = input().split()

    if command == 'END':
        break

    row, col, value = map(int, data)
    if valid_coordinates():
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*row) for row in matrix]
