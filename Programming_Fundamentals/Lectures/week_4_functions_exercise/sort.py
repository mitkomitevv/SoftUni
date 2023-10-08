def sorting_numbers(nums):
    numbers = sorted(nums)
    return numbers


input_line = [int(x) for x in input().split()]
sorted_nums = sorting_numbers(input_line)
print(sorted_nums)
