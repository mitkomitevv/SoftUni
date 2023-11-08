def characters(char1, char2):
    for char in range(ord(char_1) + 1, ord(char_2)):
        appended_list.append(chr(char))
    return appended_list


appended_list = []
char_1 = input()
char_2 = input()
result = characters(char_1, char_2)
print(' '.join(result))
