input_line1, input_line2, input_line3 = int(input()), int(input()), int(input())
students = int(input())
all_answers = input_line1 + input_line2 + input_line3 # per hour
hour = 0
while students > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    students -= all_answers
print(f'Time needed: {hour}h.')
