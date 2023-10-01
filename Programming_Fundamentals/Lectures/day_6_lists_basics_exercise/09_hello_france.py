items = input().split('|')
budget = int(input())
money = budget
list_with_new_prices = []
ticket_price = 150
profit = 0
for current_item in items:
    item = current_item.split('->')
    price = float(item[1])
    item_type = item[0]
    if price > 50.00 and item_type == 'Clothes':
        continue
    elif price > 35.00 and item_type == 'Shoes':
        continue
    elif price > 20.50 and item_type == 'Accessories':
        continue
    if money >= price:
        money -= price
        new_price = round(price * 1.4, 2)
        list_with_new_prices.append(new_price)
        profit += new_price - price
for i in list_with_new_prices:
    print(f'{i:.2f}', end=' ')
money_saved = sum(list_with_new_prices) + money
print()
print(f'Profit: {profit:.2f}')
if money_saved >= ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')
