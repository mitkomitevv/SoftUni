cards = input()
team_a = 11
team_b = 11
team_a_list = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b_list = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
flag = False
cards_list = list(cards.split(' '))
for current_card in cards_list:
    if current_card in team_a_list:
        team_a_list.remove(current_card)
        team_a -= 1
    if current_card in team_b_list:
        team_b_list.remove(current_card)
        team_b -= 1
    if team_a == 6:
        flag = True
        break
    elif team_b == 6:
        flag = True
        break
print(f'Team A - {team_a}; Team B - {team_b}')
if flag:
    print('Game was terminated')
