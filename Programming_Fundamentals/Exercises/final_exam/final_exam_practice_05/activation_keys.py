def contains(key, string):
    if string in key:
        return f"{key} contains {string}"
    return "Substring not found!"

def flip(key, up_low, start_idx, end_idx):
    for_flipping = key[start_idx:end_idx]
    if up_low == 'Upper':
        key = key[:start_idx] + for_flipping.upper() + key[end_idx:]
    elif up_low == 'Lower':
        key = key[:start_idx] + for_flipping.lower() + key[end_idx:]
    return key

def slicing(key, start_idx, end_idx):
    key = key[:start_idx] + key[end_idx:]
    return key


def main():
    activation_key = input()
    command = input().split('>>>')
    while command[0] != 'Generate':
        cmd = command[0]
        if cmd == 'Contains':
            substring = command[1]
            string = contains(activation_key, substring)
            print(string)
        elif cmd == 'Flip':
            upper_lower, start, end = command[1], int(command[2]), int(command[3])
            activation_key = flip(activation_key, upper_lower, start, end)
            print(activation_key)
        elif cmd == 'Slice':
            start, end = int(command[1]), int(command[2])
            activation_key = slicing(activation_key, start, end)
            print(activation_key)

        command = input().split('>>>')

    print(f"Your activation key is: {activation_key}")

if __name__ == '__main__':
    main()
