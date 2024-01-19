longest_intersection = set()

for _ in range(int(input())):
    data1, data2 = [x.split(',') for x in input().split('-')]

    first = set(range(int(data1[0]), int(data1[1]) + 1))
    second = set(range(int(data2[0]), int(data2[1]) + 1))

    intersection = first & second
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} "
      f"with length {len(longest_intersection)}")
