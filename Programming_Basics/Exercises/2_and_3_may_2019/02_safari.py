budget = float(input())
fuel_lt = float(input())
day = input()

day_1 = ("Saturday")
day_2 = ("Sunday")
fuel_needed = fuel_lt * 2.1
guide_price = 100

total_price = fuel_needed + guide_price

if day == day_1:
    total_price = total_price - (total_price * 0.1)
elif day == day_2:
    total_price = total_price - (total_price * 0.2)

diff = abs(total_price - budget)

if budget >= total_price:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
