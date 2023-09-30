gifts_list = list(input().split())
command = input()
while command != 'No Money':
    if 'OutOfStock' in command:
        command = command.split()
        if command[1] in gifts_list:
            for i in range(len(gifts_list)):
                gifts_list[i] = gifts_list[i].replace(command[1], 'None')
        # gifts_list = list(map(lambda x: x.replace(command[1], 'None'), gifts_list))
    elif 'Required' in command:
        command = command.split()
        index_to_replace = int(command[-1])
        if 0 <= index_to_replace < len(gifts_list):
            gifts_list[index_to_replace] = command[1]
    elif 'JustInCase' in command:
        command = command.split()
        gifts_list[-1] = command[1]
    command = input()
while 'None' in gifts_list:
    gifts_list.remove('None')
final_list = ' '.join(map(str, gifts_list))
print(final_list)
