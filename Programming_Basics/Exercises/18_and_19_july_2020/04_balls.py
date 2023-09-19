import math

balls = int(input())
total_points = 0
red, orange, yellow, white, other, black = 0, 0, 0, 0, 0, 0

for _ in range(balls):
    color_ball = input()

    if color_ball == 'red':
        total_points += 5
        red += 1
    elif color_ball == 'orange':
        total_points += 10
        orange += 1
    elif color_ball == 'yellow':
        total_points += 15
        yellow += 1
    elif color_ball == 'white':
        total_points += 20
        white += 1
    elif color_ball == 'black':
        total_points = math.floor(total_points / 2)
        black += 1
    else:
        other += 1
        continue

print(f'Total points: {total_points}')
print(f'Red balls: {red}')
print(f'Orange balls: {orange}')
print(f'Yellow balls: {yellow}')
print(f'White balls: {white}')
print(f'Other colors picked: {other}')
print(f'Divides from black balls: {black}')
