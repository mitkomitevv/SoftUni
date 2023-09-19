capacity = int(input())
cinema_income = 0
people_inside = 0

input_line = input()
while input_line != 'Movie time!':
    people_entering = int(input_line)
    people_inside += people_entering

    if people_inside > capacity:
        print('The cinema is full.')
        break

    cinema_income += people_entering * 5

    if people_entering % 3 == 0:
        cinema_income -= 5

    input_line = input()

seats_left = abs(capacity - people_inside)
if input_line == 'Movie time!':
    print(f'There are {seats_left} seats left in the cinema.')

print(f'Cinema income - {cinema_income} lv.')
