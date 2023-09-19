count_locations = int(input())

for _ in range(count_locations):
    expected_average_yield = float(input())
    days_per_location = int(input())
    total = 0
    for _ in range(days_per_location):
        total_yield_per_day = float(input())
        total += total_yield_per_day

    average_yield = total / days_per_location
    if average_yield >= expected_average_yield:
        print(f'Good job! Average gold per day: {average_yield:.2f}.')
    else:
        diff = abs(average_yield - expected_average_yield)
        print(f'You need {diff:.2f} gold.')
