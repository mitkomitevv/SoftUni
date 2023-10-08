people = int(input())
capacity = int(input())
courses = people // capacity
courses_2 = people % capacity
if courses_2 > 0:
    courses += 1
print(courses)
