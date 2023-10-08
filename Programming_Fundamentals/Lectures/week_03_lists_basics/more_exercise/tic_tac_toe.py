first_row = input().split()
second_row = input().split()
third_row = input().split()
winner = 'Draw!'
if first_row[0] == first_row[1] == first_row[2] and first_row[0] != 0:
    if first_row[0] == '1':
        winner = 'First player won'
    elif first_row[0] == '2':
        winner = 'Second player won'
elif second_row[0] == second_row[1] == second_row[2] and second_row[0] != 0:
    if second_row[0] == '1':
        winner = 'First player won'
    elif second_row[0] == '2':
        winner = 'Second player won'
elif third_row[0] == third_row[1] == third_row[2] and third_row[0] != 0:
    if third_row[0] == '1':
        winner = 'First player won'
    elif third_row[0] == '2':
        winner = 'Second player won'
if first_row[0] == second_row[1] == third_row[2] and first_row[0] != 0:
    if first_row[0] == '1':
        winner = 'First player won'
    elif first_row[0] == '2':
        winner = 'Second player won'
elif first_row[2] == second_row[1] == third_row[0] and first_row[0] != 0:
    if first_row[2] == '1':
        winner = 'First player won'
    elif first_row[2] == '2':
        winner = 'Second player won'
for i in range(3):
    if first_row[i] == second_row[i] == third_row[i] and first_row != 0:
        if first_row[i] == '1':
            winner = 'First player won'
            break
        elif first_row[i] == '2':
            winner = 'Second player won'
            break
print(winner)
