from collections import deque

clothes_box = deque(int(x) for x in input().split())
rack_capacity = int(input())
current_rack_capacity = rack_capacity
racks = 1

while clothes_box:
    cloth = clothes_box.pop()
    if current_rack_capacity >= cloth:
        current_rack_capacity -= cloth
    else:
        current_rack_capacity = rack_capacity - cloth
        racks += 1
print(racks)
