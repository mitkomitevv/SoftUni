def software_version(number):
    n1, n2, n3 = number[0], number[1], number[2]
    n3 += 1
    if n3 == 10:
        n3 = 0
        n2 += 1
        if n2 == 10:
            n2 = 0
            n1 += 1
    return f'{n1}.{n2}.{n3}'


input_line = list(map(int, input().split('.')))
print(software_version(input_line))
