import math

days = int(input())
distance_for_every_day = float(input())
total_distance = distance_for_every_day

for _ in range(days):
    percent = int(input())
    distance_for_every_day = distance_for_every_day + distance_for_every_day * percent / 100
    total_distance += distance_for_every_day

diff = math.ceil(abs(1000 - total_distance))
if total_distance >= 1000:
    print(f"You've done a great job running {diff} more kilometers!")
else:
    print(f'Sorry Mrs. Ivanova, you need to run {diff} more kilometers')