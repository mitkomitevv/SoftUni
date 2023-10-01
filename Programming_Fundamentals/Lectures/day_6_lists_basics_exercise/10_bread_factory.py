day_events = input().split('|')
energy = 100
coins = 100
for current_event in day_events:
    event_split = current_event.split('-')
    event = event_split[0]
    value = event_split[1]
    if event == 'rest':
        current_energy = energy
        energy += int(value)
        if energy >= 100:
            energy = 100
        gained = energy - current_energy
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')
    elif event == 'order':
        if energy >= 30:
            coins += int(value)
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print('You had to rest!')
            continue
    else:
        if coins >= int(value):
            coins -= int(value)
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            break
else:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')