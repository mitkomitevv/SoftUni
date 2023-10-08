race = [int(i) for i in input().split()]
middle_index = len(race) // 2
left_part, right_part = race[:middle_index], race[- 1:middle_index: - 1]
left_time, right_time = 0, 0
left, right = 'left', 'right'
counter_left, counter_right = 0, 0
while left_part and left_part[0] == 0:
    left_part = left_part[1:]
for time in left_part:
    if time == 0:
        counter_left += 0
        if counter_left > 1:
            continue
        left_time *= 0.8
    else:
        left_time += time

while right_part and right_part[0] == 0:
    right_part = right_part[1:]
for time in right_part:
    if time == 0:
        counter_right += 1
        if counter_right > 1:
            continue
        right_time *= 0.8
    else:
        right_time += time
winner = left_time if left_time < right_time else right_time
right_vs_left = left if left_time < right_time else right
print(f'The winner is {right_vs_left} with total time: {winner:.1f}')
