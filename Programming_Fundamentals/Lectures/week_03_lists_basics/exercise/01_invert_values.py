string = input()
original_list = list(map(int, string.split(' ')))
filtered_list = []
for num in original_list:
    if num < 0:
        filtered_list.append(abs(num))
    elif num > 0:
        filtered_list.append(-abs(num))
    else:
        filtered_list.append(num)
print(filtered_list)
