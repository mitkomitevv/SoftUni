n = int(input())
my_list = []
my_list_2 = []
for _ in range(n):
    data = int(input())
    if data >= 0:
        my_list.append(data)
    else:
        my_list_2.append(data)
print(my_list)
print(my_list_2)
print(f'Count of positives: {len(my_list)}')
print(f'Sum of negatives: {sum(my_list_2)}')
