n = int(input())
excluded = input()
my_list = []
for _ in range(n):
    strings = input()
    my_list.append(strings)
print(my_list)
filtered_list = []
for current_string in my_list:
    if excluded in current_string:
        filtered_list.append(current_string)
print(filtered_list)
