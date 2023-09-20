number = int(input())

first_sum = 0
second_sum = 0
for _ in range(number):
    current_number = int(input())
    first_sum += current_number

for _ in range(number):
    current_number = int(input())
    second_sum += current_number

diff = abs(first_sum - second_sum)

if first_sum == second_sum:
    print(f'Yes, sum = {second_sum}')
else:
    print(f'No, diff = {diff}')
