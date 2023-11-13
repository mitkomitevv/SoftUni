key = [int(x) for x in input().split()]
string = input()
while string != 'find':
    treasure = ''
    for idx in range(len(string)):
        treasure += chr(ord(string[idx]) - key[idx % len(key)])
    type_of_treasure = treasure.split('&')[-2]
    coordinates = treasure.split('<')[-1][0:-1]
    # some_list = treasure.split('<')
    # coordinates = some_list[1].strip('>')
    print(f"Found {type_of_treasure} at {coordinates}")

    string = input()
