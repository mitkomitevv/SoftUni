money = input()
total = 0

while money != 'NoMoreMoney':
    current_money = float(money)
    if current_money < 0:
        print('Invalid operation!')
        break
    total += current_money

    print(f'Increase: {current_money:.2f}')
    money = input()
print(f'Total: {total:.2f}')
