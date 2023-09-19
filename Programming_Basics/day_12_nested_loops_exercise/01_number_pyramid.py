n = int(input())
counter = 0
flag = 0
for row in range(1, n + 1):
    for col in range(1, row + 1):
        counter += 1
        if counter > n:
            flag = True
            break
        print(counter, end=' ')
    if flag:
        break
    print()
