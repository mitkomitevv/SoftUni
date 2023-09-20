name = input()
grade = float(input())
total_grade = grade
failed_counter = 0
expelled = False
current_grade = 1

while current_grade <= 12:
    if grade < 4.00:
        failed_counter += 1
        if failed_counter >= 2:
            expelled = True
            break
    else:
        failed_counter = 0

    current_grade += 1
    if current_grade <= 12:
        grade = float(input())
        total_grade += grade

if expelled:
    print(f"{name} has been excluded at {current_grade - 1} grade")
else:
    average_grade = total_grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
