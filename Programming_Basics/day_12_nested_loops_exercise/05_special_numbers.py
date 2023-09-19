n = int(input())

for x1 in range(1, 10):
    for x2 in range(1, 10):
        for x3 in range(1, 10):
            for x4 in range(1, 10):
                if n % x4 == 0 and n % x3 == 0 and n % x2 == 0 and n % x1 == 0:
                    print(f"{x1}{x2}{x3}{x4}", end=' ')

