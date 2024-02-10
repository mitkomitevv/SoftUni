from collections import deque

mil_caffeine = deque(int(x) for x in input().split(', '))
energy_drinks = deque(int(x) for x in input().split(', '))
total_caffeine = 0

while mil_caffeine and energy_drinks:
    caffeine = mil_caffeine.pop()
    drink = energy_drinks.popleft()
    result = caffeine * drink

    if total_caffeine + result <= 300:
        total_caffeine += result
    else:
        energy_drinks.append(drink)
        if total_caffeine - 30 < 0:
            total_caffeine = 0
        else:
            total_caffeine = total_caffeine - 30

print(f"At least Stamat wasn't exceeding the maximum caffeine." if not energy_drinks
      else f"Drinks left: {', '.join(str(x) for x in energy_drinks)}",)
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
