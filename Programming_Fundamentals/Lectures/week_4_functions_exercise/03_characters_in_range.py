char_1 = input()
char_2 = input()


def characters():
    for char in range(ord(char_1) + 1, ord(char_2)):
        print(chr(char), end=' ')


characters()
