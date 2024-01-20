rows, cols = [int(x) for x in input().split()]
matrix = [[el for el in input().split()] for x in range(rows)]
equal_cells = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        curr_el = matrix[row][col]
        next_el = matrix[row][col + 1]
        under_el = matrix[row + 1][col]
        diagonal_el = matrix[row + 1][col + 1]

        if curr_el == next_el and curr_el == under_el and curr_el == diagonal_el:
            equal_cells += 1

print(equal_cells)
