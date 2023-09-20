beginning = int(input())
end = int(input())
magic_number = int(input())
counter = 0
flag = False

for x in range(beginning, end + 1):
    for y in range(beginning, end + 1):
        counter += 1
        if x + y == magic_number:
            flag = True
            print(f'Combination N:{counter} ({x} + {y} = {magic_number})')
            break

    if flag:
        break

else:
    print(f'{counter} combinations - neither equals {magic_number}')
