string = input()
text = ''
for char in string:
    text += chr(ord(char) + 3)
    # ascii_num = ord(char) + 3
    # text += chr(ascii_num)

print(text)
