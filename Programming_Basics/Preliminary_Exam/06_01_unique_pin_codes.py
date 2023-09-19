upper_limit_n1 = int(input())
upper_limit_n2 = int(input())
upper_limit_n3 = int(input())

for n1 in range(2, upper_limit_n1 + 1, 2):
    for n2 in range(2, upper_limit_n2 + 1):
        if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:
            for n3 in range(2, upper_limit_n3 + 1, 2):
                print(f'{n1} {n2} {n3}')
