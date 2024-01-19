n = int(input())
flattened_matrix = [int(el) for _ in range(n) for el in input().split(', ')]

# flattened_matrix = []
# for _ in range(n):
#     flattened_matrix += [int(x) for x in input().split(', ')]

print(flattened_matrix)
