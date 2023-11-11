str1, str2 = input().split()
total_sum = 0
num1, num2 = 0, 0
while True:
    for char in str1:
        num1 = ord(char)
        break

    for char in str2:
        num2 = ord(char)
        break

    if str1 and str2:
        total_sum += num1 * num2
    elif str1:
        total_sum += num1
    elif str2:
        total_sum += num2

    if not str1 and not str2:
        break

    str1 = str1[1::]
    str2 = str2[1::]

print(total_sum)
