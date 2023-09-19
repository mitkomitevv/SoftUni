people = int(input())
season = input()
price = 0

if season == 'spring':
    if people <= 5:
        price = 50
    else:
        price = 48
elif season == 'summer':
    if people <= 5:
        price = 48.5
    else:
        price = 45
elif season == 'autumn':
    if people <= 5:
        price = 60
    else:
        price = 49.5
elif season == 'winter':
    if people <= 5:
        price = 86
    else:
        price = 85

total_price = people * price

if season == 'summer':
    total_price = total_price * 0.85
elif season == 'winter':
    total_price = total_price * 1.08

print(f'{total_price:.2f} leva.')