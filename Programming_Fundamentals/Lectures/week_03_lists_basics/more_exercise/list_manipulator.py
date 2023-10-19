def exchange(nums, idx):
    if 0 <= idx < len(nums):
        nums = nums[idx + 1:] + nums[:idx + 1]
    else:
        print('Invalid index')
    return nums

def max_func(cmd, nums, even_nums, odd_nums):
    if 'even' in cmd and even_nums:
        max_even_index = len(nums) - nums[::-1].index(max(even_nums)) - 1
        print(max_even_index)
    elif 'odd' in cmd and odd_nums:
        max_odd_index = len(nums) - nums[::-1].index(max(odd_nums)) - 1
        print(max_odd_index)
    else:
        print('No matches')

def min_func(cmd, nums, even_nums, odd_nums):
    if 'even' in cmd and even_nums:
        min_even_index = len(nums) - nums[::-1].index(min(even_nums)) - 1
        print(min_even_index)
    elif 'odd' in cmd and odd_nums:
        min_odd_index = len(nums) - nums[::-1].index(min(odd_nums)) - 1
        print(min_odd_index)
    else:
        print('No matches')

def first(cmd, nums, even_nums, odd_nums, count):
    if 0 < count <= len(nums):
        if 'even' in cmd:
            first_count_even = even_nums[:count]
            print(first_count_even)
        else:
            first_count_odd = odd_nums[:count]
            print(first_count_odd)
    else:
        print(f"Invalid count")

def last(cmd, nums, even_nums, odd_nums, count):
    if 0 < count <= len(nums):
        if 'even' in cmd:
            first_count_even = even_nums[-count:]
            print(first_count_even)
        else:
            first_count_odd = odd_nums[-count:]
            print(first_count_odd)
    else:
        print(f"Invalid count")

def main():
    numbers = [int(x) for x in input().split()]
    input_line = input()
    while input_line != 'end':
        command = input_line.split()
        even = [x for x in numbers if x % 2 == 0]
        odd = [x for x in numbers if x % 2 != 0]
        if 'exchange' in command:
            index = int(command[1])
            numbers = exchange(numbers, index)
        elif 'max' in command:
            max_func(command, numbers, even, odd)
        elif 'min' in command:
            min_func(command, numbers, even, odd)
        elif 'first' in command:
            first(command, numbers, even, odd, int(command[1]))
        elif 'last' in command:
            last(command, numbers, even, odd, int(command[1]))
        input_line = input()
    return numbers
print(main())
