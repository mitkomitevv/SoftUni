array = [int(x) for x in input().split()]
input_line = input().split()
while input_line[0] != 'end':
    command = input_line[0]
    if command != 'decrease':
        idx1 = int(input_line[1])
        idx2 = int(input_line[2])
    if command == 'swap':
        array[idx1], array[idx2] = array[idx2], array[idx1]
    elif command == 'multiply':
        array[idx1] = array[idx1] * array[idx2]
    elif command == 'decrease':
        array = [x - 1 for x in array]
    input_line = input().split()
print(*array, sep=', ')
