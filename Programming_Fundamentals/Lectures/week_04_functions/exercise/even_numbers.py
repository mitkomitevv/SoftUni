def even_numbers(nums):
    if nums % 2 == 0:
        return True

    return False


numbers = [int(x) for x in input().split()]
even = list(filter(even_numbers, numbers))
print(even)
