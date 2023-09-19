contract_year = input()
contract_type = input()
mobile_internet = input()
months_for_payment = int(input())
price = 0

if contract_year == 'one':
    if contract_type == 'Small':
        price = 9.98
    elif contract_type == 'Middle':
        price = 18.99
    elif contract_type == 'Large':
        price = 25.98
    elif contract_type == 'ExtraLarge':
        price = 35.99

if contract_year == 'two':
    if contract_type == 'Small':
        price = 8.58
    elif contract_type == 'Middle':
        price = 17.09
    elif contract_type == 'Large':
        price = 23.59
    elif contract_type == 'ExtraLarge':
        price = 31.79

if mobile_internet == 'yes':
    if price <= 10:
        price += 5.50
    elif 10 < price <= 30:
        price += 4.35
    else:
        price += 3.85

total = price * months_for_payment

if contract_year == 'two':
    total = total * 0.9625

print(f'{total:.2f} lv.')