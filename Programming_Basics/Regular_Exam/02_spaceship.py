width = float(input())
length = float(input())
height = float(input())
average_height = float(input())

total_volume = width * length * height
volume_room = (average_height + 0.40) * 2 * 2
total_astronauts = int(total_volume / volume_room)

if 3 <= total_astronauts <= 10:
    print(f'The spacecraft holds {total_astronauts} astronauts.')
elif total_astronauts < 3:
    print('The spacecraft is too small.')
else:
    print('The spacecraft is too big.')
