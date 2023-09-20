number = int(input())

total_first = 0
total_second = 0
for i in range(number):
    current_number = int(input())
    if i % 2 == 0:
        total_first += current_number
    else:
        total_second += current_number

diff = abs(total_first - total_second)
if total_first == total_second:
    print('Yes')
    print(f'Sum = {total_first}')
else:
    print('No')
    print(f'Diff = {diff}')
