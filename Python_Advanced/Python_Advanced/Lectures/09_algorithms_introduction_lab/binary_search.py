def binary_search(nums, target):
    left_part = 0
    right_part = len(nums) - 1

    while left_part <= right_part:
        mid = (left_part + right_part) // 2
        el = nums[mid]

        if el == target:
            return mid
        elif el > target:
            right_part = mid - 1
        elif el < target:
            left_part = mid + 1

    return -1


numbers = sorted(int(x) for x in input().split())
target_num = int(input())
print(binary_search(numbers, target_num))
