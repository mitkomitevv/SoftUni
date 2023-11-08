def palindrome(nums):
    return nums == nums[::-1]


input_line = input().split(', ')
for number in input_line:
    print(palindrome(number))
