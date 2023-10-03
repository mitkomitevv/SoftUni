budget = int(input())
money_left = budget

command = input()
while command != 'End':
    price = int(command)
    money_left -= price

    if money_left < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')
