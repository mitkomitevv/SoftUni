n = int(input())
cars = set()

for _ in range(n):
    command, number_plate = input().split(', ')
    if command == 'IN':
        cars.add(number_plate)
    else:
        if number_plate in cars:
            cars.remove(number_plate)
if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')
