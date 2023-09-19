guests = int(input())
price_for_one = float(input())
budget_desi = float(input())

if 10 <= guests <= 15:
    price_for_one = price_for_one * 0.85
elif 15 < guests <= 20:
    price_for_one = price_for_one * 0.80
elif guests > 20:
    price_for_one = price_for_one * 0.75

cake = budget_desi * 0.1

total = guests * price_for_one + cake
diff = abs(budget_desi - total)

if budget_desi >= total:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f"No party! {diff:.2f} leva needed.")