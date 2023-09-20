price_year = int(input())

shoes = price_year * 0.6
clothes = shoes * 0.8
ball = clothes / 4
accs = ball / 5

final_price = price_year + shoes + clothes + ball + accs

print(final_price)