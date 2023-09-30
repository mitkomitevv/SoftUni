input_line = input().split(' ')
shuffles = int(input())
for shuffle in range(shuffles):
    middle = len(input_line) // 2
    left_part = input_line[:middle]
    right_part = input_line[middle:]
    final_list = []
    for i in range(len(left_part)):
        final_list.append(left_part[i])
        final_list.append(right_part[i])
    input_line = final_list
print(final_list)

# 1, 2, 3, 4, 5, 6
# 1, 4, 3, 2, 5, 6
# 1, 4, 5, 2, 3, 6
# 1, 4, 2, 5, 3, 6