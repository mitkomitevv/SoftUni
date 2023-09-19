wanted_winnings = float(input())
total_money = 0
flag = False

cocktail = input()
while cocktail != 'Party!':
    number_current_cocktails = int(input())
    price_per_cocktail = len(cocktail)
    current_order = price_per_cocktail * number_current_cocktails

    if current_order % 2 != 0:
        current_order = current_order * 0.75

    total_money += current_order
    if wanted_winnings <= total_money:
        flag = True
        break

    cocktail = input()

diff = abs(wanted_winnings - total_money)
if flag:
    print('Target acquired.')
else:
    print(f'We need {diff:.2f} leva more.')

print(f'Club income - {total_money:.2f} leva.')
