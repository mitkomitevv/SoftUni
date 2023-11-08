input_line = input().split()
lowered = [word.lower() for word in input_line]
my_list = []
for word in lowered:
    if lowered.count(word) % 2 != 0:
        if word not in my_list:
            my_list.append(word)
print(' '.join(my_list))