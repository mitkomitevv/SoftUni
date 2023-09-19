import sys

number = int(input())
total = 0
max_number = -sys.maxsize
for _ in range(number):
    current_number = int(input())
    total += current_number

    if current_number > max_number:
        max_number = current_number

if total - max_number == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(max_number - (total - max_number))
    print('No')
    print(f'Diff = {diff}')
