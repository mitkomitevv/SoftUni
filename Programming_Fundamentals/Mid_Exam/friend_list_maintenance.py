usernames = input().split(', ')
input_line = input().split()
blacklisted = 0
lost_names = 0
while input_line[0] != 'Report':
    command = input_line[0]
    if command == 'Blacklist':
        name = input_line[1]
        if name in usernames:
            index = usernames.index(name)
            usernames[index] = 'Blacklisted'
            blacklisted += 1
            print(f'{name} was blacklisted.')
        else:
            print(f'{name} was not found.')
    elif command == 'Error':
        index = int(input_line[1])
        if 0 <= index < len(usernames):
            if usernames[index] != 'Blacklisted' and usernames[index] != 'Lost':
                print(f'{usernames[index]} was lost due to an error.')
                usernames[index] = 'Lost'
                lost_names += 1
    elif command == 'Change':
        index = int(input_line[1])
        name = input_line[2]
        if 0 <= index < len(usernames):
            old_name = usernames[index]
            usernames[index] = name
            print(f'{old_name} changed his username to {name}.')

    input_line = input().split()

print(f'Blacklisted names: {blacklisted}')
print(f'Lost names: {lost_names}')
print(*usernames)
