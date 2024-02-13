from collections import deque

bowls_ramen = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))

while bowls_ramen and customers:
    ramen, customer = bowls_ramen.pop(), customers.popleft()

    if ramen == customer:
        continue
    elif ramen > customer:
        bowls_ramen.append(ramen - customer)
    else:
        customers.appendleft(customer - ramen)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
