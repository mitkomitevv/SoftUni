width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
all_boxes = 0
flag = False

input_line = input()
while input_line != 'Done':
    boxes = int(input_line)
    all_boxes += boxes

    if all_boxes > volume:
        flag = True
        break

    input_line = input()

diff = abs(all_boxes - volume)
if flag:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')
