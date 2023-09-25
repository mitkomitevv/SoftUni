first_string = input()
second_string = input()
last_string = first_string
for char_index in range(len(first_string)):
    left_side = second_string[:char_index + 1]
    right_side = first_string[char_index + 1:]
    finished_string = left_side + right_side
    if finished_string != last_string:
        print(finished_string)
        last_string = finished_string

for curr_index in range(len(first_string)):
    left_side = second_string[:curr_index + 1]
    right_side = first_string[curr_index + 1::]
    print(f'{left_side}{right_side}')# first_string = input()                               lecturer's solution
# second_string = input()
# last_printed_string = first_string
# for character_index in range(len(first_string)):
#     left_part = second_string[:character_index + 1]
#     right_part = first_string[character_index + 1:]
#     new_string = left_part + right_part
#     if new_string != last_printed_string:
#         print(new_string)
#         last_printed_string = new_string
