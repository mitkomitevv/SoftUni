hour_exam = int(input())
min_exam = int(input())
arrival_hour = int(input())
arrival_min = int(input())

all_exam_min = (hour_exam * 60) + min_exam
all_arrival_min = (arrival_hour * 60) + arrival_min
diff_min = abs(all_arrival_min - all_exam_min)

if all_exam_min < all_arrival_min:
    print("Late")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")

elif all_arrival_min == all_exam_min or diff_min <= 30:
    print("On time")
    if diff_min <= 30:
        print(f"{diff_min} minutes before the start")

else:
    print("Early")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")
