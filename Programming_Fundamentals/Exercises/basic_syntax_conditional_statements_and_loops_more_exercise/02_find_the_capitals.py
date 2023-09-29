string = input()
my_list = []
for i in range(len(string)):
    if string[i].isupper():
        my_list.append(i)
print(my_list)
