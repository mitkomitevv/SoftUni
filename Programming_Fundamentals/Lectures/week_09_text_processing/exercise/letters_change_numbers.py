some_string = input().split()
total_sum = 0

for string in some_string:
    first = string[0]
    second = string[-1]
    number = int(string[1:-1])
    if first.isupper():
        total_sum += number / (ord(first) - 64)
    elif first.islower():
        total_sum += number * (ord(first) - 96)

    if second.isupper():
        total_sum -= ord(second) - 64
    elif second.islower():
        total_sum += ord(second) - 96

print(f'{total_sum:.2f}')