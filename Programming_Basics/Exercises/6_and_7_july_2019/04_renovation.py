import math

height = int(input())
width = int(input())
percent_not_for_painting = int(input())
for_painting = height * width * 4
total_for_painting = math.ceil(for_painting - (for_painting * (percent_not_for_painting / 100)))
input_line = input()
while input_line != 'Tired!':
    litres = int(input_line)
    total_for_painting -= litres
    if total_for_painting == 0:
        print('All walls are painted! Great job, Pesho!')
        break
    if total_for_painting < 0:
        print(f'All walls are painted and you have {abs(total_for_painting)} l paint left!')
        break

    input_line = input()

else:
    print(f'{total_for_painting} quadratic m left.')