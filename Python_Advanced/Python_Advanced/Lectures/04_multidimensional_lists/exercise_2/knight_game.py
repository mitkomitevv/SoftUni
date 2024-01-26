def knight_moves(board, removed, no_knights):
    max_attacks = 0
    max_knight = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'K':
                attacks = 0
                for x, y in possible_moves:
                    r, c = row + x, col + y

                    if valid_move(r, c):
                        if board[r][c] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    max_knight = [row, col]

    if max_knight:
        row, col = max_knight
        board[row][col] = '0'
        removed += 1
        return board, removed, no_knights
    else:
        no_knights = False
        return board, removed, no_knights

def valid_move(r, c):
    if 0 <= r < len(chess_board) and 0 <= c < len(chess_board):
        return True
    return False

chess_board = [[el for el in input()] for _ in range(int(input()))]

possible_moves = (
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2)
)
flag = True
removed_knights = 0
while True:
    if flag:
        chess_board, removed_knights, flag = knight_moves(chess_board, removed_knights, flag)
    else:
        break

print(removed_knights)
