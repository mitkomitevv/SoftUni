bad_grades = int(input())
task_number = 0
failed_task = 0
all_grades = 0
last_task = ''
task_name = input()
while task_name != 'Enough':
    grade = int(input())
    last_task = task_name
    if grade <= 4:
        failed_task += 1
    if failed_task == bad_grades:
        print(f'You need a break, {failed_task} poor grades.')
        break
    task_number += 1
    all_grades += grade
    task_name = input()
else:
    avg_grade = all_grades / task_number
    print(f'Average score: {avg_grade:.2f}')
    print(f'Number of problems: {task_number}')
    print(f'Last problem: {last_task}')
