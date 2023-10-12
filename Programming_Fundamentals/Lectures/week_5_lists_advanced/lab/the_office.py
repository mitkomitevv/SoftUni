def happy_or_not(happiness, num):
    employee_happiness = [int(x) * num for x in happiness]
    average_happiness = (sum(employee_happiness) / len(employee_happiness))
    happy_employees = [x for x in employee_happiness if x >= average_happiness]
    message = 'happy' if len(happy_employees) >= len(employee_happiness) / 2 else 'not happy'
    return f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are {message}!'


input_line = input().split()
factor = int(input())
print(happy_or_not(input_line, factor))
