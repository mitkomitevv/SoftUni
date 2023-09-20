hour = int(input())
minutes = int(input())

total_hours = hour * 60
time_total_min = total_hours + minutes + 15

final_hour = time_total_min // 60
final_min = time_total_min % 60

if final_hour > 23:
    final_hour = 0

print(f"{final_hour}:{final_min:02}")