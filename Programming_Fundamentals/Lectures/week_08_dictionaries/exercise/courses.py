input_line = input()
courses = {}
while input_line != 'end':
    course, name = input_line.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
    input_line = input()

for course, names in courses.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")