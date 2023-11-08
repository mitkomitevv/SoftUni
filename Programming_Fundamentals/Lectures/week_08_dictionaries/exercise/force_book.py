input_line = input()
force_users = {}
while input_line != 'Lumpawaroo':
    if '|' in input_line:
        side, user = input_line.split(' | ')
        flag = True
        for users in force_users.values():
            if user in users:
                flag = False
                break
        if flag:
            if side not in force_users:
                force_users[side] = []
            force_users[side].append(user)

    elif '->' in input_line:
        user, side = input_line.split(' -> ')
        for users in force_users.values():
            if user in users:
                users.remove(user)
                break
        if side not in force_users:
            force_users[side] = []
        force_users[side].append(user)
        print(f"{user} joins the {side} side!")

    input_line = input()

for side, name_list in force_users.items():
    if name_list:
        print(f"Side: {side}, Members: {len(name_list)}")
        for member in name_list:
            print(f'! {member}')