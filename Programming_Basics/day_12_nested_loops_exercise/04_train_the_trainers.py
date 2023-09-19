jury_number = int(input())
grades_count = 0
sum_all_grades = 0

input_line = input()
while input_line != 'Finish':
    presentation = input_line

    sum_current_grades = 0
    for _ in range(jury_number):
        current_grade = float(input())
        sum_current_grades += current_grade
        sum_all_grades += current_grade
        grades_count += 1

    avg_current_grade = sum_current_grades / jury_number
    print(f'{presentation} - {avg_current_grade:.2f}.')

    input_line = input()

avg_all_grades = sum_all_grades / grades_count
print(f"Student's final assessment is {avg_all_grades:.2f}.")
