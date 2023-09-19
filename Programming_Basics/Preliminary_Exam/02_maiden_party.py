price_for_party = float(input())
number_love_letters = int(input())
number_roses = int(input())
number_keychains = int(input())
number_caricatures = int(input())
number_lucky = int(input())

count_products = number_love_letters + number_roses + number_keychains + number_caricatures + number_lucky
money = (number_love_letters * 0.6) + (number_roses * 7.2) + (number_keychains * 3.6) + (number_caricatures * 18.2) + \
        (number_lucky * 22)

if count_products > 25:
    money = money * 0.65

hosting_price = money * 0.1
total_money = money - hosting_price
diff = abs(total_money - price_for_party)
if money >= price_for_party:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
