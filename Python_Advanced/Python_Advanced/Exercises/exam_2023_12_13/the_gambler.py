def valid_move(n, cr, cc):
    if 0 <= cr < n and 0 <= cc < n:
        return True


size = int(input())
matrix = []
player_pos = []
money = 100
jackpot_won, left_boundary = False, False

for row in range(size):
    matrix.append([el for el in input()])
    if 'G' in matrix[row]:
        player_pos = [row, matrix[row].index('G')]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

direction = input()
while money > 0 and direction != 'end':
    matrix[player_pos[0]][player_pos[1]] = '-'
    move_direction = directions[direction]
    r, c = player_pos[0] + move_direction[0], player_pos[1] + move_direction[1]

    if valid_move(size, r, c):
        if matrix[r][c] == 'W':
            money += 100
        elif matrix[r][c] == 'P':
            money -= 200
        elif matrix[r][c] == 'J':
            money += 100000
            jackpot_won = True
            matrix[r][c] = '-'
            player_pos = [r, c]
            break

        matrix[r][c] = '-'
        player_pos = [r, c]
    else:
        left_boundary = True
        break
    direction = input()

matrix[player_pos[0]][player_pos[1]] = 'G'
if left_boundary or money <= 0:
    print("Game over! You lost everything!")
elif jackpot_won:
    print(f"You win the Jackpot!\n"
          f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in matrix]
else:
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in matrix]
