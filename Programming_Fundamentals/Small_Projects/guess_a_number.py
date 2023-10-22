from random import randint

def guess_number():
    computer_number = randint(1, 1000)
    moves_counter = 0
    while True:
        player_input = input("Guess the number (1-1000): ")
        moves_counter += 1
        if not player_input.isnumeric():
            print('Invalid input. Try again...')
            continue
        player_number = int(player_input)

        if player_number == computer_number:
            print('You guessed it!')
            break
        elif player_number > computer_number:
            print('Too high!')
        else:
            print('Too low!')

        if moves_counter == 9:
            print('Too many tries.')
            break
guess_number()
while True:
    player = input("Play again? y or n: ")
    if player == 'y':
        guess_number()
    else:
        exit()
