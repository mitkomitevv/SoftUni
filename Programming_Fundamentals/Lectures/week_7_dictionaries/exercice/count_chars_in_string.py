text = input()
my_dict = {}
for letter in text:
    if letter != ' ':
        if letter not in my_dict.keys():
            my_dict[letter] = 0
        my_dict[letter] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")


# text = input()
# my_dict = {}
# for letter in text:
#     if letter != ' ':
#         if letter not in my_dict:
#             my_dict[letter] = 1
#         else:
#             my_dict[letter] += 1
#
# for char in my_dict:
#     print(f"{char} -> {my_dict[char]}")