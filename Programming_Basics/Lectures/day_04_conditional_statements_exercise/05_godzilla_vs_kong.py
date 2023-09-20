film_budget = float(input())
extras = int(input())
clothes_extras = float(input())

if extras > 150:
    clothes_extras = clothes_extras - (clothes_extras * 0.1)

money_for_clothes = extras * clothes_extras
decor = film_budget * 0.1
total = money_for_clothes + decor

diff = abs(total - film_budget)

if total > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
