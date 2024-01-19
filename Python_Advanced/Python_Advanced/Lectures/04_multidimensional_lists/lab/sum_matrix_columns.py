rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col_idx in range(cols):
    total = 0
    for row_idx in range(rows):
        total += matrix[row_idx][col_idx]
    print(total)
