player_one = input()
player_two = input()
one_points_counter = 0
two_points_counter = 0
winner = ''
winning_points = 0
war = False

input_line = input()
while input_line != 'End of game':
    card_player_one = int(input_line)
    card_player_two = int(input())

    if card_player_one > card_player_two:
        one_points_counter += card_player_one - card_player_two

    elif card_player_two > card_player_one:
        two_points_counter += card_player_two - card_player_one

    elif card_player_two == card_player_one:
        war = True
        break

    input_line = input()

if war:
    card_player_one = int(input())
    card_player_two = int(input())
    if card_player_one > card_player_two:
        winner = player_one
        winning_points = one_points_counter
    elif card_player_two > card_player_one:
        winner = player_two
        winning_points = two_points_counter
    print('Number wars!')
    print(f'{winner} is winner with {winning_points} points')
else:
    print(f'{player_one} has {one_points_counter} points')
    print(f'{player_two} has {two_points_counter} points')


# if war:
#     card_player_one = int(input())
#     card_player_two = int(input())
#     if card_player_one > card_player_two:
#         winner = player_one
#         winning_points = card_player_one - card_player_two
#     elif card_player_two > card_player_one:
#         winner = player_two
#         winning_points = card_player_two - card_player_one
#     print('Number wars!')
#     print(f'{winner} is winner with {winning_points} points')
# else:
#     print(f'{player_one} has {one_points_counter} points')
#     print(f'{player_two} has {two_points_counter} points')

# if one_points_counter > two_points_counter:
#     winner = player_one
#     winning_points = one_points_counter
# elif two_points_counter > one_points_counter:
#     winner = player_two
#     winning_points = two_points_counter
#
# if war:
#     print('Number wars!')
#     print(f'{winner} is winner with {winning_points} points')
# else:
#     print(f'{player_one} has {one_points_counter} points')
#     print(f'{player_two} has {two_points_counter} points')

