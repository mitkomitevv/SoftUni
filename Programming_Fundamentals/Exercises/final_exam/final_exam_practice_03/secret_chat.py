def insert_space(message, idx):
    message = message[:idx] + ' ' + message[idx:]
    return message

def reverse(message, string):
    if string in message:
        message = message.replace(string, '', 1)
        rev_str = string[::-1]
        message += rev_str
        return message
    return 'error'

def change_all(message, old_str, new_str):
    if old_str in message:
        return message.replace(old_str, new_str)
    return message

def main():
    concealed_message = input()
    input_line = input()
    while input_line != 'Reveal':
        command = input_line.split(':|:')
        cmd = command[0]
        if cmd == 'InsertSpace':
            index = int(command[1])
            concealed_message = insert_space(concealed_message, index)
            print(concealed_message)
        elif cmd == 'Reverse':
            substring = command[1]
            result = reverse(concealed_message, substring)
            if result == 'error':
                print(result)
            else:
                concealed_message = result
                print(concealed_message)
        elif cmd == 'ChangeAll':
            substring, replacement = command[1], command[2]
            concealed_message = change_all(concealed_message, substring, replacement)
            print(concealed_message)

        input_line = input()

    print(f"You have a new text message: {concealed_message}")

if __name__ == '__main__':
    main()