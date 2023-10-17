target_sequence = [int(x) for x in input().split()]
input_line = input().split()
while input_line[0] != 'End':
    command = input_line[0]
    index = int(input_line[1])
    p_v_r = int(input_line[2])
    if command == 'Shoot':
        if 0 <= index < len(target_sequence):
            target_sequence[index] -= p_v_r
            if target_sequence[index] <= 0:
                target_sequence.pop(index)
    elif command == 'Add':
        if 0 <= index < len(target_sequence):
            target_sequence.insert(index, p_v_r)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        start = index - p_v_r
        end = index + p_v_r + 1
        if 0 <= start < end < len(target_sequence):
            del target_sequence[start:end]
        else:
            print('Strike missed!')
    input_line = input().split()
print(*target_sequence, sep='|')
