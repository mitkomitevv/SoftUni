destination = input()
total_money = 0
money = 0
while destination != 'End':
    needed_money = float(input())
    while total_money < needed_money:
        money = float(input())
        total_money += money
        if total_money >= needed_money:
            print(f'Going to {destination}!')
            total_money = 0
            break

    destination = input()
