from collections import deque

water_quantity = int(input())
name = input()
queue_people = deque()

while name != 'Start':
    queue_people.append(name)
    name = input()

command = input().split()

while command[0] != 'End':
    if "refill" in command:
        water_quantity += int(command[1])
    else:
        water_needed = int(command[0])
        if water_quantity >= water_needed:
            water_quantity -= water_needed
            print(f"{queue_people.popleft()} got water" )
        else:
            print(f"{queue_people.popleft()} must wait")

    command = input().split()

print(f"{water_quantity} liters left")
