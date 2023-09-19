product = input()
count_product = int(input())
day = int(input())
price = 0
total_price = 0

if day <= 15:
    if product == 'Cake':
        price = 24
    elif product == 'Souffle':
        price = 6.66
    elif product == 'Baklava':
        price = 12.6
elif day > 15:
    if product == 'Cake':
        price = 28.7
    elif product == 'Souffle':
        price = 9.8
    elif product == 'Baklava':
        price = 16.98

total_price = count_product * price

if day <= 22:
    if 100 <= total_price <= 200:
        total_price = total_price * 0.85
    elif total_price > 200:
        total_price = total_price * 0.75

if day <= 15:
    total_price = total_price * 0.90

print(f'{total_price:.2f}')
