number = input()
largest_number = 0
numbers = []
sorted_list = []
for num in number:
    numbers.append(num)
    sorted_list = sorted(numbers, reverse=True)
    largest_number = ''.join(sorted_list)
print(largest_number)
