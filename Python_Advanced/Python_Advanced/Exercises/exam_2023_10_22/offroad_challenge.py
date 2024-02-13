from collections import deque

fuel_quantities = deque(int(n) for n in input().split())
consumption = deque(int(n) for n in input().split())
quantity = deque(int(n) for n in input().split())
reached, initial_len_quantity = 0, len(quantity)

while fuel_quantities:
    fuel, index, needed_fuel = fuel_quantities.pop(), consumption.popleft(), quantity.popleft()
    result = fuel - index

    if result >= needed_fuel:
        reached += 1
    else:
        break

if reached > 0:
    [print(f"John has reached: Altitude {i}") for i in range(1, reached + 1)]
if reached < initial_len_quantity:
    print(f"John did not reach: Altitude {initial_len_quantity - len(quantity)}")
if reached == initial_len_quantity:
    print("John has reached all the altitudes and managed to reach the top!")
elif reached and reached < initial_len_quantity:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(f'Altitude {i}' for i in range(1, reached + 1))}")
else:
    print(f"John failed to reach the top.\n"
          f"John didn't reach any altitude.")
