matrix = [[x for x in input()] for _ in range(int(input()))]
searched_symbol = input()
found = False

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == searched_symbol:
            found = True
            print(f'({i}, {j})')
            break
    if found:
        break
else:
    print(f'{searched_symbol} does not occur in the matrix')
