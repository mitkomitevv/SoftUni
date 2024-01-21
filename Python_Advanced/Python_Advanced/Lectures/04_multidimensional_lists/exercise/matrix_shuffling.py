rows, cols = [int(n) for n in input().split()]
matrix = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(rows)]

while True:
    command, *data = input().split()

    if command == 'END':
        break

    if command != 'swap' or len(data) != 4:
        print("Invalid input!")
        continue
    else:
        valid_data = [el for el in data if el.isdigit() and int(el) >= 0]

        if len(valid_data) != 4:
            print("Invalid input!")
            continue
        row1, col1, row2, col2 = map(int, valid_data)
        if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*el) for el in matrix]
        else:
            print("Invalid input!")
