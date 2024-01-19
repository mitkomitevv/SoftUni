rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
max_sub_matrix_sum = float('-inf')
row1, row2 = [], []

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        current_element = matrix[row_idx][col_idx]
        next_element = matrix[row_idx][col_idx + 1]
        under_element = matrix[row_idx + 1][col_idx]
        diagonal_element = matrix[row_idx + 1][col_idx + 1]
        current_sum = current_element + next_element + under_element + diagonal_element
        if current_sum > max_sub_matrix_sum:
            max_sub_matrix_sum = current_sum
            row1, row2 = [matrix[row_idx][col_idx], matrix[row_idx][col_idx + 1]], [matrix[row_idx + 1][col_idx], matrix[row_idx + 1][col_idx + 1]]

print(*row1)
print(*row2)
print(max_sub_matrix_sum)
