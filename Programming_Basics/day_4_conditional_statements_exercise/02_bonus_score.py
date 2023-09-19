number = int(input())

points = 0

if number <= 100:
    points = 5
elif 1000 > number > 100:
    points = number * 0.2
else:
    points = number * 0.1

if number % 2 == 0:
    points = points + 1
elif number % 10 == 5:
    points = points + 2

total_points = number + points

print(points)
print(total_points)
