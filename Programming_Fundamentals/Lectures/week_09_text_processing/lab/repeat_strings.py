string = input().split()
for word in string:
    print(''.join(word * len(word)), end='')
