def print_numbers(nums):
    negative_sum = sum(x for x in nums if x < 0)
    positive_sum = sum(x for x in nums if x > 0)

    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')

numbers = [int(x) for x in input().split()]
print_numbers(numbers)
