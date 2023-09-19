sold_games = int(input())
hearthstone, fornite, overwatch, others = 0, 0, 0, 0

for _ in range(sold_games):
    current_game = input()
    if current_game == 'Hearthstone':
        hearthstone += 1
    elif current_game == 'Fornite':
        fornite += 1
    elif current_game == 'Overwatch':
        overwatch += 1
    else:
        others += 1

hearthstone_percent = hearthstone / sold_games * 100
fornite_percent = fornite / sold_games * 100
overwatch_percent = overwatch / sold_games * 100
others_percent = others / sold_games * 100

print(f'Hearthstone - {hearthstone_percent:.2f}%')
print(f'Fornite - {fornite_percent:.2f}%')
print(f'Overwatch - {overwatch_percent:.2f}%')
print(f'Others - {others_percent:.2f}%')