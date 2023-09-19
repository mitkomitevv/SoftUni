name = input()
year_counter = 0
fail_counter = 0
total_grades = 0
expelled = False

while year_counter != 12:
    current_grade = float(input())
    if current_grade < 4:
        fail_counter += 1

        if fail_counter > 2:
            expelled = True
            break

        continue

    else:
        total_grades += current_grade
        year_counter += 1

avg_grade = total_grades / year_counter
if expelled:
    print(f'{name} has been excluded at {year_counter + 1} grade')
else:
    print(f'{name} graduated. Average grade: {avg_grade:.2f}')
