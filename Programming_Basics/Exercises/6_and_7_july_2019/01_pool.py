from math import ceil

number_of_people = int(input())
entry_price = float(input())
chair_price = float(input())
umbrella_price = float(input())

money_entry = number_of_people * entry_price
umbrellas = ceil(number_of_people * 0.5) * umbrella_price
chairs = ceil(number_of_people * 0.75) * chair_price

total = money_entry + umbrellas + chairs

print(f"{total:.2f}" + ' lv' + '.')