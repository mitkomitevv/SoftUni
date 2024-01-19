matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]

diagonal_sum = 0
for row_index in range(len(matrix)):
    diagonal_sum += matrix[row_index][row_index]

# for row_idx in range(len(matrix)):
#     for col_idx in range(len(matrix)):
#         if row_idx == col_idx:
#             diagonal_sum += matrix[row_idx][col_idx]

print(diagonal_sum)
