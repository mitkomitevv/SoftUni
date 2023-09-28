n = int(input())
my_list = []
filtered_list = []
for _ in range(n):
    num = int(input())
    my_list.append(num)
command = input()
for nums in my_list:
    if command == 'even' and nums % 2 == 0:
        filtered_list.append(nums)
    elif command == 'odd' and nums % 2 != 0:
        filtered_list.append(nums)
    elif command == 'negative' and nums < 0:
        filtered_list.append(nums)
    elif command == 'positive' and nums >= 0:
        filtered_list.append(nums)
print(filtered_list)
