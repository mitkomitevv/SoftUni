budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
number_of_loaves = 0
colored_eggs = 0
bread_price = flour_price + eggs_price + milk_price
money_left = budget
while True:
    if money_left < bread_price:
        break
    number_of_loaves += 1
    money_left -= bread_price
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2
print(f'You made {number_of_loaves} loaves of Easter bread!'
      f' Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
