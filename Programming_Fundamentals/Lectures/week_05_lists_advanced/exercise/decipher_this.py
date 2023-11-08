def message_deciphered(string):
    deciphered = []
    for word in string:
        word = list(word)
        characters = [x for x in word if not x.isnumeric()]
        numbers = int(''.join([x for x in word if x.isnumeric()]))
        ascii_letter = chr(numbers)
        characters[0], characters[-1] = characters[-1], characters[0]
        ready_word = ascii_letter + ''.join(characters)
        deciphered.append(ready_word)
    return ' '.join(deciphered)


input_line = input().split()
print(message_deciphered(input_line))
