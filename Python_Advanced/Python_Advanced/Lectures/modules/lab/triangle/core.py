def print_triangle(num):
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()

    for row in range(num, 0, -1):
        for col in range(1, row):
            print(col, end=' ')
        print()