matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]

primary = [matrix[r][r] for r in range(len(matrix))]
secondary = [matrix[r][len(matrix) - r - 1] for r in range(len(matrix))]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
