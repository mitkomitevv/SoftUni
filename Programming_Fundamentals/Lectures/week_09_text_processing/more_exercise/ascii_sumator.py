first, second, string = ord(input()), ord(input()), input()
total_sum = 0
for char in string:
    if first < ord(char) < second:
        total_sum += ord(char)
print(total_sum)