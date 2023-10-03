# numbers = list(map(int, input().split()))
numbers = input().split()
strings = input()
message = []
for number in numbers:
    sum_of_index = 0
    for index in number:
        sum_of_index += int(index)
    sum_of_index %= len(strings)
    message.append(strings[sum_of_index])
    strings = strings[:sum_of_index] + strings[sum_of_index + 1:]
print(''.join(message))
