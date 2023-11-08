from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
bonus = int(input())
max_student = 0
max_bonus = 0
for i in range(1, number_of_students + 1):
    attendance = int(input())
    total_bonus = (attendance / number_of_lectures) * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_student = attendance
print(f"Max Bonus: {ceil(max_bonus)}.\n"
      f"The student has attended {max_student} lectures.")
