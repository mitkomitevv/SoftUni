from collections import deque

chocolate = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))
milkshakes = 0

while chocolate and milk and milkshakes < 5:
    curr_chocolate = chocolate.pop()
    curr_milk = milk.popleft()

    if curr_chocolate <= 0 and curr_milk <= 0:
        continue
    elif curr_chocolate <= 0:
        milk.appendleft(curr_milk)
        continue
    elif curr_milk <= 0:
        chocolate.append(curr_chocolate)
        continue

    if curr_chocolate == curr_milk:
        milkshakes += 1
    else:
        milk.append(curr_milk)
        chocolate.append(curr_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")
