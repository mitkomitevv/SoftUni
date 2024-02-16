def valid_capture_left(pos, capture):
    return 0 <= pos[0] + capture['left'][0] < SIZE and 0 <= pos[1] + capture['left'][1] < SIZE


def valid_capture_right(pos, capture):
    return 0 <= pos[0] + capture['right'][0] < SIZE and 0 <= pos[1] + capture['right'][1] < SIZE


SIZE = 8
chess_board = []
white_pos, black_pos = [], []
white_move, black_move = [-1, 0], [1, 0]
white_capture, black_capture = {'left': [-1, -1], 'right': [-1, 1]}, {'left': [1, -1], 'right': [1, 1]}
rows = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
cols = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

for row in range(SIZE):
    chess_board.append(input().split())
    if 'w' in chess_board[row]:
        white_pos = [row, chess_board[row].index('w')]
    if 'b' in chess_board[row]:
        black_pos = [row, chess_board[row].index('b')]


while True:

    if valid_capture_left(white_pos, white_capture) and chess_board[white_pos[0] + white_capture['left'][0]][white_pos[1] + white_capture['left'][1]] == 'b':
        r, c = white_pos[0] + white_capture['left'][0], white_pos[1] + white_capture['left'][1]
        white_pos = [r, c]
        chess_board[r][c] = 'w'
        coord = cols[c] + rows[r]
        print(f"Game over! White win, capture on {coord}.")
        break
    elif valid_capture_right(white_pos, white_capture) and chess_board[white_pos[0] + white_capture['right'][0]][white_pos[1] + white_capture['right'][1]] == 'b':
        r, c = white_pos[0] + white_capture['right'][0], white_pos[1] + white_capture['right'][1]
        white_pos = [r, c]
        chess_board[r][c] = 'w'
        coord = cols[c] + rows[r]
        print(f"Game over! White win, capture on {coord}.")
        break
    else:
        r, c = white_pos[0] + white_move[0], white_pos[1] + white_move[1]
        chess_board[white_pos[0]][white_pos[1]] = '-'
        white_pos = [r, c]
        chess_board[r][c] = 'w'
        if r == 0:
            coord = cols[c] + rows[r]
            print(f"Game over! White pawn is promoted to a queen at {coord}.")
            break


    if valid_capture_left(black_pos, black_capture) and chess_board[black_pos[0] + black_capture['left'][0]][black_pos[1] + black_capture['left'][1]] == 'w':
        r, c = black_pos[0] + black_capture['left'][0], black_pos[1] + black_capture['left'][1]
        black_pos = [r, c]
        chess_board[r][c] = 'b'
        coord = cols[c] + rows[r]
        print(f"Game over! Black win, capture on {coord}.")
        break
    elif valid_capture_right(black_pos, black_capture) and chess_board[black_pos[0] + black_capture['right'][0]][black_pos[1] + black_capture['right'][1]] == 'w':
        r, c = black_pos[0] + black_capture['right'][0], black_pos[1] + black_capture['right'][1]
        black_pos = [r, c]
        chess_board[r][c] = 'b'
        coord = cols[c] + rows[r]
        print(f"Game over! Black win, capture on {coord}.")
        break
    else:
        r, c = black_pos[0] + black_move[0], black_pos[1] + black_move[1]
        chess_board[black_pos[0]][black_pos[1]] = '-'
        black_pos = [r, c]
        chess_board[r][c] = 'b'
        if r == 7:
            coord = cols[c] + rows[r]
            print(f"Game over! Black pawn is promoted to a queen at {coord}.")
            break
