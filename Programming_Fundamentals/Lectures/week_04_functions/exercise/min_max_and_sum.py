def min_number(nums):
    min_n = min(nums)
    return min_n


def max_number(nums):
    max_n = max(nums)
    return max_n


def sum_numbers(nums):
    sum_n = sum(nums)
    return sum_n


input_line = [int(x) for x in input().split()]
print(f'The minimum number is {min_number(input_line)}')
print(f'The maximum number is {max_number(input_line)}')
print(f'The sum number is: {sum_numbers(input_line)}')
