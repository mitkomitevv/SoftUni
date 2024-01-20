matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

primary = sum([matrix[r][r] for r in range(len(matrix))])
secondary = sum([matrix[r][len(matrix) - r - 1] for r in range(len(matrix))])
print(abs(primary - secondary))
