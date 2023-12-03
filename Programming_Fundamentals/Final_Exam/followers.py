def new_follower(followers_dict, username):
    if username not in followers_dict:
        followers_dict[username] = [0, 0]
    return followers_dict

def like(followers_dict, username, count):
    if username not in followers_dict:
        followers_dict[username] = [count, 0]
        return followers_dict
    followers_dict[username][0] += count
    return followers_dict

def comment(followers_dict, username):
    if username not in followers_dict:
        followers_dict[username] = [0, 1]
        return followers_dict
    followers_dict[username][1] += 1
    return followers_dict

def blocked(followers_dict, username):
    if username in followers_dict:
        del followers_dict[username]
        return followers_dict
    return f"{username} doesn't exist."

def printing(followers_dict):
    print(f"{len(followers_dict)} followers")
    for name, values in followers_dict.items():
        print(f"{name}: {sum(values)}")

def main():
    followers_dict = {}
    line = input().split(': ')
    while line[0] != 'Log out':
        command = line[0]
        if command == 'New follower':
            username = line[1]
            followers_dict = new_follower(followers_dict, username)
        elif command == 'Like':
            username, count = line[1], int(line[2])
            followers_dict = like(followers_dict, username, count)
        elif command == 'Comment':
            username = line[1]
            followers_dict = comment(followers_dict, username)
        elif command == 'Blocked':
            username = line[1]
            result = blocked(followers_dict, username)
            if isinstance(result, str):
                print(result)
            else:
                followers_dict = result

        line = input().split(': ')

    printing(followers_dict)

if __name__ == '__main__':
    main()
