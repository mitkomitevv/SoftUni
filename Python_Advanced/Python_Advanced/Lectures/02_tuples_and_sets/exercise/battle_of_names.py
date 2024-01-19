even = set()
odd = set()

for n in range(1, int(input()) + 1):
    sum_name = sum(ord(char) for char in input()) // n
    even.add(sum_name) if sum_name % 2 == 0 else odd.add(sum_name)

if sum(even) == sum(odd):
    print(*odd.union(even), sep=', ')
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=', ')
else:
    print(*odd.symmetric_difference(even), sep=', ')
