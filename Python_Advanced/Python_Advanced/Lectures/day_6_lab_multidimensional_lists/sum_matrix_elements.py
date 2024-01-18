rows, cols = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for _ in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.append(col)
    total_sum += sum(col)

# for cell in matrix:
#     total_sum += sum(cell)

print(total_sum)
print(matrix)
