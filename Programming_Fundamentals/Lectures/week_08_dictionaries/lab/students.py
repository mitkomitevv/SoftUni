input_line = input()
students = {}
while ":" in input_line:
    student, ID, course = input_line.split(':')
    course = "_".join(course.split())
    students[student] = [ID, course]

    input_line = input()

for student in students:
    if input_line in students[student]:
        print(f"{student} - {students[student][0]}")