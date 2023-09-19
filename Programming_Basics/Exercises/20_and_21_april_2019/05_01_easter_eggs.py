number = int(input())
red_eggs, orange_eggs, blue_eggs, green_eggs = 0, 0, 0, 0
max_eggs_color = 0
max_eggs = ''

for _ in range(number):
    current_color = input()
    if current_color == 'red':
        red_eggs += 1
    elif current_color == 'orange':
        orange_eggs += 1
    elif current_color == 'blue':
        blue_eggs += 1
    elif current_color == 'green':
        green_eggs += 1

    if red_eggs > max_eggs_color:
        max_eggs_color = red_eggs
        max_eggs = 'red'
    elif orange_eggs > max_eggs_color:
        max_eggs_color = orange_eggs
        max_eggs = 'orange'
    elif blue_eggs > max_eggs_color:
        max_eggs_color = blue_eggs
        max_eggs = 'blue'
    elif green_eggs > max_eggs_color:
        max_eggs_color = green_eggs
        max_eggs = 'green'


# max_eggs = max([red_eggs, orange_eggs, blue_eggs, green_eggs])

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_eggs_color} -> {max_eggs}')
