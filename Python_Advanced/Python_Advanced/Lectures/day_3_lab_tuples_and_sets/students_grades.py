number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    grades_str = ' '.join(f"{g:.2f}" for g in grades)
    print(f"{name} -> {grades_str} (avg: {avg_grade:.2f})")
