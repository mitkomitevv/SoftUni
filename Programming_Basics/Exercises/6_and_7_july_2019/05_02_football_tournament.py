team_name = input()
matches = int(input())
total_points = 0
wins, draws, loses = 0, 0, 0

if matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    for _ in range(matches):
        current_match = input()
        if current_match == 'W':
            total_points += 3
            wins += 1
        elif current_match == 'D':
            total_points += 1
            draws += 1
        elif current_match == 'L':
            loses += 1

    win_rate = wins / matches * 100

    print(f'{team_name} has won {total_points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {loses}')
    print(f'Win rate: {win_rate:.2f}%')
