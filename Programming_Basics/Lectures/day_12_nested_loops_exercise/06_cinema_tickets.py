student_tickets = 0
standard_tickets = 0
kid_tickets = 0

total_tickets = 0

input_line = input()
while input_line != 'Finish':
    movie = input_line
    free_seats = int(input())

    current_tickets = 0
    input_two = input()
    while input_two != 'End':
        if input_two == "Finish":
            break
        ticket_kind = input_two
        current_tickets += 1
        total_tickets += 1

        if ticket_kind == 'student':
            student_tickets += 1
        elif ticket_kind == 'standard':
            standard_tickets += 1
        else:
            kid_tickets += 1

        if current_tickets == free_seats:
            break

        input_two = input()

    capacity = current_tickets / free_seats * 100
    print(f'{movie} - {capacity:.2f}% full.')

    input_line = input()

percentage_student = student_tickets / total_tickets * 100
percentage_standard = standard_tickets / total_tickets * 100
percentage_kid = kid_tickets / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f'{percentage_student:.2f}% student tickets.')
print(f'{percentage_standard:.2f}% standard tickets.')
print(f'{percentage_kid:.2f}% kids tickets.')