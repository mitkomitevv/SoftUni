rows, cols = [int(n) for n in input().split()]
start = ord('a')

for row in range(start, start + rows):
    for col in range(cols):
        print(f'{chr(row)}{chr(col + row)}{chr(row)}', end=' ')
    print()
