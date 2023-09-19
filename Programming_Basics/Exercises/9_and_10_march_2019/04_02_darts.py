player = input()
starting_points = 301
successful_shots = 0
failed_shots = 0

input_line = input()
while input_line != 'Retire':
    ring = input_line
    points = int(input())
    remaining_points = starting_points

    if ring == 'Single':
        starting_points -= points
    elif ring == 'Double':
        starting_points -= points * 2
    elif ring == 'Triple':
        starting_points -= points * 3

    if starting_points < 0:
        starting_points = remaining_points
        failed_shots += 1
        input_line = input()
        continue

    successful_shots += 1

    if starting_points == 0:
        print(f'{player} won the leg with {successful_shots} shots.')
        break

    input_line = input()

if input_line == 'Retire':
    print(f'{player} retired after {failed_shots} unsuccessful shots.')