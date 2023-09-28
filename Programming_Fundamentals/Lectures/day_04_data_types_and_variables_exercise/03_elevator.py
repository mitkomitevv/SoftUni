people = int(input())
capacity = int(input())
courses = people // capacity
courses_2 = people % capacity
if courses_2 > 0:
    courses += 1
if capacity >= people:
    print("All the persons fit inside the elevator. Only one course is needed.")
else:
    print(courses)
