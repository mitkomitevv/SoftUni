target = int(input())
money = 0

while True:
    if money >= target:
        break

    service = input()
    if service == 'closed':
        break
    type_of_service = input()

    if service == 'haircut':
        if type_of_service == 'mens':
            money += 15
        elif type_of_service == 'ladies':
            money += 20
        elif type_of_service == 'kids':
            money += 10

    elif service == 'color':
        if type_of_service == 'touch up':
            money += 20
        elif type_of_service == 'full color':
            money += 30

diff = abs(target - money)
if money >= target:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {diff}lv. more.')

print(f'Earned money: {money}lv.')