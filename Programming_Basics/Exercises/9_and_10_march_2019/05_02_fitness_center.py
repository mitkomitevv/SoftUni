input_line = int(input())
back, chest, legs, abs_workout, protein_shake, protein_bar = 0, 0, 0, 0, 0, 0

for _ in range(input_line):
    current_line = input()
    if current_line == 'Back':
        back += 1
    elif current_line == 'Chest':
        chest += 1
    elif current_line == 'Legs':
        legs += 1
    elif current_line == 'Abs':
        abs_workout += 1
    elif current_line == 'Protein shake':
        protein_shake += 1
    elif current_line == 'Protein bar':
        protein_bar += 1

total_people = back + chest + legs + abs_workout + protein_shake + protein_bar
training_people = back + chest + legs + abs_workout
protein_people = protein_shake + protein_bar
percentage_training = training_people / total_people * 100
percentage_protein = protein_people / total_people * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs_workout} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{percentage_training:.2f}% - work out')
print(f'{percentage_protein:.2f}% - protein')
