budget = float(input())
shows_number = int(input())

total = 0
for _ in range(shows_number):
    show_name = input()
    price_show = float(input())
    if show_name == 'Thrones':
        total += price_show * 0.5
    elif show_name == 'Lucifer':
        total += price_show * 0.6
    elif show_name == 'Protector':
        total += price_show * 0.7
    elif show_name == 'TotalDrama':
        total += price_show * 0.8
    elif show_name == 'Area':
        total += price_show * 0.9
    else:
        total += price_show

diff = abs(total - budget)

if budget >= total:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')