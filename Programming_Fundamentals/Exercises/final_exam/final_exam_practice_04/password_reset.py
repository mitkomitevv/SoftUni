def take_odd(string):
    string = [string[x] for x in range(1, len(string), 2)]
    return ''.join(string)

def cut(string, index, length):
    for_removing = string[index:index + length]
    return string.replace(for_removing, '', 1)

def substitute(string, old_string, new_string):
    if old_string in string:
        return string.replace(old_string, new_string)
    return "Nothing to replace!"

def main():
    string = input()
    input_line = input()
    while input_line != "Done":
        input_line = input_line.split()
        command = input_line[0]
        if command == 'TakeOdd':
            string = take_odd(string)
            print(string)
        elif command == 'Cut':
            index, length = int(input_line[1]), int(input_line[2])
            string = cut(string, index, length)
            print(string)
        elif command == 'Substitute':
            substring, replacement = input_line[1], input_line[2]
            result = substitute(string, substring, replacement)
            if result == "Nothing to replace!":
                print(result)
            else:
                string = result
                print(string)

        input_line = input()

    print(f"Your password is: {string}")

if __name__ == '__main__':
    main()
