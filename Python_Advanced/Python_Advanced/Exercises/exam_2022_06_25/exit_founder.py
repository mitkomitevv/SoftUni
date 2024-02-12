SIZE = 6
player1, player2 = input().split(', ')

matrix = [[col for col in input().split()] for row in range(SIZE)]
rest1, rest2 = '', ''

while True:

    r, c = [int(x) for x in input().strip('(').strip(')').split(', ')]
    if player1 == rest1:
        rest1 = ''
    elif matrix[r][c] == 'E':
        print(f"{player1} found the Exit and wins the game!" )
        break
    elif matrix[r][c] == 'T':
        print(f"{player1} is out of the game! The winner is {player2}.")
        break
    elif matrix[r][c] == 'W':
        rest1 = player1
        print(f"{player1} hits a wall and needs to rest.")

    r, c = [int(x) for x in input().strip('(').strip(')').split(', ')]
    if player2 == rest2:
        rest2 = ''
    elif matrix[r][c] == 'E':
        print(f"{player2} found the Exit and wins the game!")
        break
    elif matrix[r][c] == 'T':
        print(f"{player2} is out of the game! The winner is {player1}.")
        break
    elif matrix[r][c] == 'W':
        rest2 = player2
        print(f"{player2} hits a wall and needs to rest.")
