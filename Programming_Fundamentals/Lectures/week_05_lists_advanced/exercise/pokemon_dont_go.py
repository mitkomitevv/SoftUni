distance = list(map(int, input().split()))
sum_elements = 0
while len(distance) > 0:
    index = int(input())
    if index < 0:
        element_popped = distance.pop(0)
        element_copy = distance[-1]
        distance.insert(0, element_copy)
    elif index > len(distance) - 1:
        element_popped = distance.pop()
        element_copy = distance[0]
        distance.insert(distance[-1], element_copy)
    else:
        element_popped = distance.pop(index)
    distance = [x + element_popped if x <= element_popped else x - element_popped for x in distance]
    sum_elements += element_popped
print(sum_elements)
