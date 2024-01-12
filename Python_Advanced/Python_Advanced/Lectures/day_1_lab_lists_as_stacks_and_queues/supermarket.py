from collections import deque

name = input()
queue_people = deque()

while name != 'End':
    if name != 'Paid':
        queue_people.append(name)
    else:
        while queue_people:
            print(queue_people.popleft())

    name = input()

print(f"{len(queue_people)} people remaining.")
