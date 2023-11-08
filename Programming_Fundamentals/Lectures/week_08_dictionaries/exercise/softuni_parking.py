def register(users, name, license_plate):
    if name not in users:
        users[name] = license_plate
        print(f"{name} registered {users[name]} successfully")
    else:
        print(f"ERROR: already registered with plate number {users[name]}")

def unregister(users, name):
    if name not in users:
        print(f"ERROR: user {name} not found")
    else:
        print(f"{name} unregistered successfully")
        del users[name]

def main():
    n = int(input())
    users = {}

    for _ in range(n):
        input_line = input().split()
        name = input_line[1]

        if 'register' in input_line:
            license_plate = input_line[2]
            register(users, name, license_plate)
        elif 'unregister' in input_line:
            unregister(users, name)

    for key, value in users.items():
        print(f"{key} => {value}")

    return users

if __name__ == '__main__':
    main()