import math

number_of_guests = int(input())
budget = int(input())

bread_number = math.ceil(number_of_guests / 3)
eggs_number = number_of_guests * 2

price_bread = bread_number * 4
price_eggs = eggs_number * 0.45

total = price_bread + price_eggs
diff = abs(budget - total)

if budget >= total:
    print(f"Lyubo bought {bread_number} Easter bread and {eggs_number} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
