budget = float(input())
total_money = 0
discount_counter = 0
all_counter = 0
flag = False

name_product = input()
while name_product != 'Stop':
    product_price = float(input())
    discount_counter += 1
    all_counter += 1

    if discount_counter == 3:
        product_price /= 2
        discount_counter = 0

    total_money += product_price

    if total_money > budget:
        flag = True
        break

    name_product = input()

diff = abs(budget - total_money)
if flag:
    print(f"You don't have enough money!")
    print(f'You need {diff:.2f} leva!')
else:
    print(f'You bought {all_counter} products for {total_money:.2f} leva.')