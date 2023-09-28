n = int(input())
my_list = []
filtered_list = []
for _ in range(n):
    num = int(input())
    my_list.append(num)
command = input()
for number in my_list:
    if command == 'even' and number % 2 == 0:
        filtered_list.append(number)
    elif command == 'odd' and number % 2 != 0:
        filtered_list.append(number)
    elif command == 'negative' and number < 0:
        filtered_list.append(number)
    elif command == 'positive' and number >= 0:
        filtered_list.append(number)
print(filtered_list)
