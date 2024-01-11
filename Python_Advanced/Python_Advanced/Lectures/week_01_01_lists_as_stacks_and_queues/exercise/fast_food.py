from collections import deque

quantity_food = int(input())
all_orders = deque(int(x) for x in input().split())
all_orders_copy = all_orders.copy()
print(max(all_orders))

for current_order in all_orders:
    if quantity_food >= current_order:
        quantity_food -= current_order
        all_orders_copy.popleft()
    else:
        print("Orders left:", end=' ')
        print(*all_orders_copy)
        break
else:
    print("Orders complete")
