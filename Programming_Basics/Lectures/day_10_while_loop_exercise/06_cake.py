width = int(input())
length = int(input())
available_pieces = width * length
all_pieces = 0
flag = False
input_line = input()
while input_line != 'STOP':
    taken_pieces = int(input_line)
    available_pieces -= taken_pieces

    if all_pieces > available_pieces:
        flag = True
        break

    input_line = input()

diff = abs(all_pieces - available_pieces)
if flag:
    print(f'No more cake left! You need {diff} pieces more.')
else:
    print(f'{diff} pieces are left.')
