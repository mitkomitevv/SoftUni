most_points = 0
winner = ''

input_line = input()
while input_line != 'Stop':
    name = input_line
    current_points = 0

    for x in range(len(name)):
        number = int(input())

        if ord(name[x]) == number:
            points = 10
        else:
            points = 2

        current_points += points

    if current_points >= most_points:
        most_points = current_points
        winner = name

    input_line = input()

print(f'The winner is {winner} with {most_points} points!')
