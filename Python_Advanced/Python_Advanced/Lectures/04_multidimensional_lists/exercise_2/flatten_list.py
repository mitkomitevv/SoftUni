# flat = [int(num) for els in input().split('|')[::-1] for num in els.split()]

print(*[int(num) for els in input().split('|')[::-1] for num in els.split()])

# result = []
#
# for els in line:
#     numbers = [int(num) for num in els.split()]
#
#     result.extend(numbers)
#
# print(*result)
