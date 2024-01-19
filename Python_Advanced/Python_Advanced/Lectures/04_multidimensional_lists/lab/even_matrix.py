rows = int(input())
matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for _ in range(rows)]
# matrix = []
# for _ in range(rows):
#     numbers = [int(x) for x in input().split(', ')]
#     matrix.append([x for x in numbers if x % 2 == 0])

print(matrix)
