num = int(input())
p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(num):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif 200 <= current_number < 400:
        p2 += 1
    elif 400 <= current_number < 600:
        p3 += 1
    elif 600 <= current_number < 800:
        p4 += 1
    else:
        p5 += 1

p1_percentage = p1 / num * 100
p2_percentage = p2 / num * 100
p3_percentage = p3 / num * 100
p4_percentage = p4 / num * 100
p5_percentage = p5 / num * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')