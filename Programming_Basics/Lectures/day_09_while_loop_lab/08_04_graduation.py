name = input()
year_counter = 0
fail_counter = 0
total_grades = 0

while year_counter != 12:
    current_grade = float(input())

    if current_grade < 4:
        fail_counter += 1

        if fail_counter > 1:
            print(f'{name} has been excluded at {year_counter + 1} grade')
            break

        continue

    else:
        total_grades += current_grade
        year_counter += 1

    if year_counter == 12:
        avg_grade = total_grades / year_counter
        print(f'{name} graduated. Average grade: {avg_grade:.2f}')
        break
