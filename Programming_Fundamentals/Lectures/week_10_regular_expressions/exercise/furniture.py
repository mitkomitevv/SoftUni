import re

line = input()
total_money = 0
pattern = r'([A-Za-z]+)<<([\d]+\.?[\d]*)!([\d]+)'
print('Bought furniture:')
while line != 'Purchase':
    match = re.search(pattern, line)
    if match:
        furniture, price, amount = match.groups()
        total_money += float(price) * int(amount)
        print(furniture)
    line = input()
print(f"Total money spend: {total_money:.2f}")
