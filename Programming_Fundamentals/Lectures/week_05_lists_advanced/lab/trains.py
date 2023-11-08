def train(num):
    train_list = [0] * num
    input_line = input()
    while input_line != 'End':
        command = input_line.split()
        counter = 0
        if command[0] == 'add':
            popped = train_list.pop()
            counter += int(command[1]) + int(popped)
            train_list.append(counter)
        elif command[0] == 'insert':
            train_list[int(command[1])] = int(command[2]) + train_list[int(command[1])]
        elif command[0] == 'leave':
            train_list[int(command[1])] = train_list[int(command[1])] - int(command[2])
        input_line = input()
    return train_list


number = int(input())
print(train(number))
