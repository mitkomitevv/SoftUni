budget_vacation = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
trucks_count = int(input())

price_puzzle = puzzle_count * 2.60
price_dolls = dolls_count * 3
price_teddy = teddy_count * 4.10
price_minions = minions_count * 8.20
price_trucks = trucks_count * 2

toys_count = puzzle_count + dolls_count + teddy_count + minions_count + trucks_count
sum_total = price_puzzle + price_dolls + price_teddy + price_minions + price_trucks

if toys_count >= 50:
    sum_total = sum_total - (sum_total * 0.25)

money_made = sum_total - (sum_total * 0.1)

diff = abs(budget_vacation - money_made)

if money_made >= budget_vacation:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
