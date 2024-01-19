intersection = set()
longest_intersection = set()

for _ in range(int(input())):
    first, second = (tuple(int(n) for n in x.split(',')) for x in input().split('-'))
    intersection.clear()

    for num in range(first[0], first[1] + 1):
        for num2 in range(second[0], second[1] + 1):
            if num2 == num:
                intersection.add(num2)
            if len(longest_intersection) < len(intersection):
                longest_intersection = intersection.copy()

longest_intersection = list(longest_intersection)
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
