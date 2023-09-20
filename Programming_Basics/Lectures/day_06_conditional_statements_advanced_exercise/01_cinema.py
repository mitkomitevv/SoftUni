type_of_projection = input()
rows = int(input())
columns = int(input())

income = 0
number_of_seats = rows * columns

if type_of_projection == 'Premiere':
    income = number_of_seats * 12.00
elif type_of_projection == 'Normal':
    income = number_of_seats * 7.50
elif type_of_projection == 'Discount':
    income = number_of_seats * 5.00

print(f'{income:.2f} leva')