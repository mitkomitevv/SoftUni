def remove_vowels(char):
    new_string = [x for x in char if x not in letters_to_remove]
    return new_string


letters_to_remove = 'a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I'
input_line = input()
print(''.join(remove_vowels(input_line)))
