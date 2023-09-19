number = int(input())
current_number = int(input())
sum_numbers = 0

while number > sum_numbers:
    sum_numbers += current_number

    if sum_numbers >= number:
        print(sum_numbers)
        break

    current_number = int(input())
