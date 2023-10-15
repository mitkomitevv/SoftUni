input_line = input()
taken = []
number_list = [int(x) for x in input_line if x.isdigit()]
string_list = [x for x in input_line if not x.isdigit()]
take_list = [x for i, x in enumerate(number_list) if i % 2 == 0]
skip_list = [x for i, x in enumerate(number_list) if i % 2 != 0]
for i in range(len(take_list)):
    taken_chars = string_list[:take_list[i]]
    string_list = string_list[take_list[i]:]
    string_list = string_list[skip_list[i]:]
    taken += taken_chars
print(''.join(taken))
