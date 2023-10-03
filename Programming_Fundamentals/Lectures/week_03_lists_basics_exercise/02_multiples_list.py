factor = int(input())
count = int(input())
counter = 0
my_list = []
for _ in range(count):
    my_list.append(factor + counter)
    counter += factor
print(my_list)
