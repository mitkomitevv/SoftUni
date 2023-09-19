budget = float(input())
overnight_stay = int(input())
price_overnight = float(input())
percent_extra_expense = int(input())

if overnight_stay > 7:
    price_overnight = price_overnight - (price_overnight * 0.05)

price_for_sleep = overnight_stay * price_overnight
extra_expense = budget * (percent_extra_expense / 100)
total = price_for_sleep + extra_expense

if total > budget:
    print(f"{total - budget:.2f}" ' leva' + ' needed' + '.')
else:
    print(f"Ivanovi will be left with {budget - total:.2f} leva after vacation.")