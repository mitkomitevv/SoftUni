from Python_Advanced.Python_Advanced.Lectures.modules.lab.fibonacci_sequence.core import create_sequence, locate_number

input_line = input().split()
fibonacci = []

while input_line != 'Stop':
    command = input_line[0]
    if command == 'Create':
        num = int(input_line[2])
        fibonacci = create_sequence(num)

    elif command == 'Locate':
        num = int(input_line[1])
        locate_number(fibonacci, num)

    input_line = input().split()