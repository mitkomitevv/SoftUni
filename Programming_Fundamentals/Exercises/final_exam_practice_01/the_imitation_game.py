message = list(input())
instructions = input()

while instructions != 'Decode':
    parts = instructions.split('|')
    command = parts[0]
    if command == 'Move':
        number = int(parts[1])
        message = message[number:] + message[:number]
    elif command == 'Insert':
        index, value = int(parts[1]), parts[2]
        message = message[:index] + list(value) + message[index:]
    elif command == 'ChangeAll':
        substring, replacement = parts[1], parts[2]
        message = ''.join(message).replace(substring, replacement)
        message = list(message)

    instructions = input()

print(f"The decrypted message is: {''.join(message)}")

# 83/100 in judge
# message = list(input())
# instructions = input()
# while instructions != 'Decode':
#     instructions = instructions.split('|')
#     command = instructions[0]
#     if command == 'Move':
#         number = int(instructions[1])
#         message = message[number:] + message[:number]
#     elif command == 'Insert':
#         index, value = int(instructions[1]), instructions[2]
#         message.insert(index, value)
#     elif command == 'ChangeAll':
#         substring, replacement = instructions[1], instructions[2]
#         for idx in range(len(message)):
#             if message[idx] == substring:
#                 message[idx] = replacement
#     instructions = input()
#
# print(f"The decrypted message is: {''.join(message)}")
