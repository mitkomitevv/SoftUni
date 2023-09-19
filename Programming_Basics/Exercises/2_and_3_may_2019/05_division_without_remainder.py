number = int(input())
p1, p2, p3 = 0, 0, 0

for _ in range(number):
    current_number = int(input())
    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1

p1_percentage = p1 / number * 100
p2_percentage = p2 / number * 100
p3_percentage = p3 / number * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
