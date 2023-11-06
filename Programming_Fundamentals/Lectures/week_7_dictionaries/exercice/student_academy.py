num = int(input())
students = {}

for _ in range(num):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    students[key] = sum(value) / len(value)

students = {key: value for key, value in students.items() if value >= 4.50}

for name, grade in students.items():
    print(f"{name} -> {grade:.2f}")
