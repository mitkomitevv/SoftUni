tournaments = int(input())
starting_points = int(input())
points_from_tournaments = 0
wins = 0

for _ in range(tournaments):
    current_tournament = (input())
    if current_tournament == 'W':
        points_from_tournaments += 2000
        wins += 1
    elif current_tournament == 'F':
        points_from_tournaments += 1200
    elif current_tournament == 'SF':
        points_from_tournaments += 720

final_points = starting_points + points_from_tournaments
avg_points = int(points_from_tournaments / tournaments)
percentage_wins = wins / tournaments * 100

print(f'Final points: {final_points}')
print(f'Average points: {avg_points}')
print(f'{percentage_wins:.2f}%')