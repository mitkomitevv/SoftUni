while True:
    string = input()
    if string == 'End':
        break
    if string == 'SoftUni':
        continue
    for char in string:
        print(f'{char * 2}', end='')
    print()

# current_string = input()                   lecturer's solution
# while current_string != "End":
#     if current_string != "SoftUni":
#         new_string = ""
#         for character in current_string:
#             new_string += character * 2
#         print(new_string)
#     current_string = input()
