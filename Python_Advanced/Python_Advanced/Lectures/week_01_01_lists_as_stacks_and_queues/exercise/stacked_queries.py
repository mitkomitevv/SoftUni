from collections import deque

n = int(input())
stack_nums = deque()

for _ in range(n):
    command = input().split()
    if command[0] == '1':
        stack_nums.append(int(command[1]))
    elif command[0] == '2' and stack_nums:
        stack_nums.pop()
    elif command[0] == '3' and stack_nums:
        print(max(stack_nums))
    elif command[0] == '4' and stack_nums:
        print(min(stack_nums))

# stack_nums = [str(x) for x in stack_nums]
# reversed_nums = [str(stack_nums.pop()) for _ in range(len(stack_nums))]
# if stack_nums:
#     stack_nums.reverse()
#     print(", ".join(str(x) for x in stack_nums))
stack_nums.reverse()
print(*stack_nums, sep=", ")