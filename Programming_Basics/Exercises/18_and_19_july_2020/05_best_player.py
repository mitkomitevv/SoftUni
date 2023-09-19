best_player = ''
most_goals = 0
input_line = input()
while input_line != 'END':
    player_name = input_line
    goals = int(input())

    if goals > most_goals:
        most_goals = goals
        best_player = player_name

    if goals >= 10:
        break

    input_line = input()

print(f'{best_player} is the best player!')
if most_goals >= 3:
    print(f'He has scored {most_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {most_goals} goals.')
