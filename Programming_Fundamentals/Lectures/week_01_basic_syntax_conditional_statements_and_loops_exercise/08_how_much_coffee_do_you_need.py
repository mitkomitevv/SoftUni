counter = 0
input_line = input()
while input_line != 'END':
    event = input_line
    if event == 'coding' or event == 'dog' or event == 'cat' or event == 'movie':
        counter += 1
    elif event == 'CODING' or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
        counter += 2
    input_line = input()
if counter > 5:
    print("You need extra sleep")
else:
    print(counter)

# coffee_counter = 0                         lecturer's solution
# command = input()
# while command != "END":
#     if command.lower() == "coding" \
#             or command.lower() == "dog" \
#             or command.lower() == "cat" \
#             or command.lower() == "movie":
#         if command.islower():
#             coffee_counter += 1
#         else: # if command.isupper()
#             coffee_counter += 2
#     command = input()
# if coffee_counter > 5:
#     print("You need extra sleep")
# else:
#     print(coffee_counter)
