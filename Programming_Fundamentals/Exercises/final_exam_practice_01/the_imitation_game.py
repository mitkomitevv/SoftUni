message = list(input())
instructions = input()
while instructions != 'Decode':
    instructions = instructions.split('|')
    command = instructions[0]
    if command == 'Move':
        number = int(instructions[1])
        message = message[number:] + message[:number]
    elif command == 'Insert':
        index, value = int(instructions[1]), instructions[2]
        message.insert(index, value)
    elif command == 'ChangeAll':
        substring, replacement = instructions[1], instructions[2]
        for idx in range(len(message)):
            if message[idx] == substring:
                message[idx] = replacement
    instructions = input()

print(f"The decrypted message is: {''.join(message)}")
