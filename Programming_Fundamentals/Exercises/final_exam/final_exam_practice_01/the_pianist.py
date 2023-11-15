def add(dictionary, piece, composer, key):
    if piece in dictionary:
        return dictionary, f"{piece} is already in the collection!"
    dictionary[piece] = []
    dictionary[piece] += [composer, key]
    return dictionary, f"{piece} by {composer} in {key} added to the collection!"

def remove(dictionary, piece):
    if piece in dictionary:
        del dictionary[piece]
        return dictionary, f"Successfully removed {piece}!"
    return dictionary, f"Invalid operation! {piece} does not exist in the collection."

def change(dictionary, piece, new_key):
    if piece in dictionary:
        dictionary[piece][1] = new_key
        return dictionary, f"Changed the key of {piece} to {new_key}!"
    return dictionary, f"Invalid operation! {piece} does not exist in the collection."

def printing(dictionary):
    for key, value in dictionary.items():
        print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")

def main():
    number_of_pieces = int(input())
    some_dict = {}
    for _ in range(number_of_pieces):
        pieces = input().split('|')
        piece, composer, key = pieces[0], pieces[1], pieces[2]
        if piece not in some_dict:
            some_dict[piece] = []
        some_dict[piece] += [composer, key]

    input_line = input()
    while input_line != 'Stop':
        command = input_line.split('|')
        cmd, piece = command[0], command[1]
        if cmd == 'Add':
            composer, key = command[2], command[3]
            some_dict, message = add(some_dict, piece, composer, key)
            print(message)
        elif cmd == 'Remove':
            some_dict, message = remove(some_dict, piece)
            print(message)
        elif cmd == 'ChangeKey':
            new_key = command[2]
            some_dict, message = change(some_dict, piece, new_key)
            print(message)

        input_line = input()

    printing(some_dict)

if __name__ == '__main__':
    main()