import math

record_sec = float(input())
distance_m = float(input())
time_m = float(input())

sec_total = distance_m * time_m
delay = math.floor(distance_m / 15) * 12.5
total_time = sec_total + delay

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_sec:.2f} seconds slower.")
