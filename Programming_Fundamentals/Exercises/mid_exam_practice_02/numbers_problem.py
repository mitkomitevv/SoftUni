starting_list = [int(x) for x in input().split()]
average = sum(starting_list) / len(starting_list)
list_of_biggest = [x for x in starting_list if x > average]
sorted_list = sorted(list_of_biggest, reverse=True)
if len(sorted_list) == 0:
    print('No')
    exit()
while len(sorted_list) > 5:
    sorted_list.pop()
print(*sorted_list)
