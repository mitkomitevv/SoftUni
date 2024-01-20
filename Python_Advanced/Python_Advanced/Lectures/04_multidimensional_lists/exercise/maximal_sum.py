rows, cols = [int(x) for x in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = float('-inf')
biggest_cell = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col+3]                       #matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]
        second_row = matrix[row + 1][col:col+3]                  #matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]
        third_row = matrix[row + 2][col:col+3]                   #matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_cell = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_cell]
