import sys

first_num = int(input())
second_num = int(input())

for num in range(first_num, second_num + 1):
    num_to_str = str(num)
    even_sum = 0
    odd_sum = 0
    for i in range(0, len(num_to_str)):
        digit = int(num_to_str[i])

        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(num, end=' ')
