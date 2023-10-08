key = int(input())
number_of_lines = int(input())
for _ in range(number_of_lines):
    letter = input()
    decrypted = ord(letter) + key
    print(chr(decrypted), end='')
