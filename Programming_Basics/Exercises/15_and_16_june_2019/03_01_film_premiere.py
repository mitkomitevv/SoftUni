movie = input()
packet = input()
tickets = int(input())

price = 0
if movie == 'John Wick':
    if packet == 'Drink':
        price = 12
    elif packet == 'Popcorn':
        price = 15
    elif packet == 'Menu':
        price = 19
if movie == 'Star Wars':
    if packet == 'Drink':
        price = 18
    elif packet == 'Popcorn':
        price = 25
    elif packet == 'Menu':
        price = 30
if movie == 'Jumanji':
    if packet == 'Drink':
        price = 9
    elif packet == 'Popcorn':
        price = 11
    elif packet == 'Menu':
        price = 14

total_price = tickets * price

if movie == 'Star Wars' and tickets >= 4:
    total_price = total_price * 0.7
elif movie == 'Jumanji' and tickets == 2:
    total_price = total_price * 0.85

print(f'Your bill is {total_price:.2f} leva.')
