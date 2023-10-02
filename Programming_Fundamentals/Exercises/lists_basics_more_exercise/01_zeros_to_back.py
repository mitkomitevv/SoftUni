strings = input().split(', ')
str_to_int = [int(x) for x in strings]
count_0 = str_to_int.count(0)
removed_0 = [x for x in str_to_int if x != 0]
formatted = removed_0 + [0] * count_0
print(formatted)
# formatted = removed_0
# for i in range(count_0):
#     formatted.append(0)
# print(formatted)
