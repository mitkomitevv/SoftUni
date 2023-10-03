divisor = int(input())
boundary = int(input())
max_number = 0
for current_number in range(1, boundary + 1):
    if current_number % divisor == 0:
        max_number = current_number
print(f'{max_number}')

# divisor = int(input())
# boundary = int(input())
# for number in range(boundary, divisor - 1, -1):
#     if number % divisor == 0:
#         break
# print(number)
