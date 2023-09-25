first_string = input()
second_string = input()

for curr_index in range(len(first_string)):
    left_side = second_string[:curr_index + 1]
    right_side = first_string[curr_index + 1::]
    print(f'{left_side}{right_side}')