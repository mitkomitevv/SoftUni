data = [int(x) for x in input().split()]
input_line = input()
left, right = 0, 0

while input_line != 'end':
    command = input_line.split()
    even_numbers = [x for x in data if x % 2 == 0]
    odd_numbers = [x for x in data if x % 2 != 0]

    if 'exchange' in command:
        if len(data) > int(command[1]) >= 0:
            left, right = data[:int(command[1]) + 1], data[int(command[1]) + 1:]
            data = right + left
        else:
            print('Invalid index')

    elif 'max' in command:
        if 'odd' in command and odd_numbers:
            max_odd_i = len(data) - data[::-1].index(max(odd_numbers)) - 1
            print(max_odd_i)
        elif 'even' in command and even_numbers:
            max_even_i = len(data) - data[::-1].index(max(even_numbers)) - 1
            print(max_even_i)
        else:
            print('No matches')

    elif 'min' in command:
        if 'odd' in command and odd_numbers:
            min_odd_i = len(data) - data[::-1].index(min(odd_numbers)) - 1
            print(min_odd_i)
        elif 'even' in command and even_numbers:
            min_even_i = len(data) - data[::-1].index(min(even_numbers)) - 1
            print(min_even_i)
        else:
            print('No matches')

    elif 'first' in command:
        if int(command[1]) <= len(data):
            if 'odd' in command:
                first_count_odd = odd_numbers[:int(command[1])]
                print(first_count_odd)
            elif 'even' in command:
                first_count_even = even_numbers[:int(command[1])]
                print(first_count_even)
        else:
            print('Invalid count')

    elif 'last' in command:
        if int(command[1]) <= len(data):
            if 'odd' in command:
                last_count_odd = odd_numbers[-int(command[1]):]
                print(last_count_odd)
            elif 'even' in command:
                last_count_even = even_numbers[-int(command[1]):]
                print(last_count_even)
        else:
            print('Invalid number')
    input_line = input()

print(data)
