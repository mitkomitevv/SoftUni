def drive(dictionary_cars, vehicle, distance, gas):
    if dictionary_cars[vehicle][1] < gas:
        return "Not enough fuel to make that ride"
    dictionary_cars[vehicle][0] += distance
    dictionary_cars[vehicle][1] -= gas
    if dictionary_cars[vehicle][0] > 100000:
        print(f"{vehicle} driven for {distance} kilometers. {gas} liters of fuel consumed.")
        del dictionary_cars[vehicle]
        return f"Time to sell the {vehicle}!"
    return dictionary_cars

def refuel(dictionary_cars, vehicle, gas):
    if dictionary_cars[vehicle][1] + gas > 75:
        gas = 75 - dictionary_cars[vehicle][1]
        dictionary_cars[vehicle][1] = 75
        return dictionary_cars, gas
    dictionary_cars[vehicle][1] += gas
    return dictionary_cars, gas

def revert(dictionary_cars, vehicle, km):
    dictionary_cars[vehicle][0] -= km
    if dictionary_cars[vehicle][0] < 10000:
        dictionary_cars[vehicle][0] = 10000
        return dictionary_cars, False
    return dictionary_cars, True

def main():
    num_cars = int(input())
    cars = {}
    for _ in range(num_cars):
        input_line = input().split('|')
        car, mileage, fuel = input_line[0], int(input_line[1]), int(input_line[2])
        if car not in cars:
            cars[car] = []
        cars[car] += [mileage, fuel]

    input_line2 = input()
    while input_line2 != 'Stop':
        input_line2 = input_line2.split(' : ')
        command, car = input_line2[0], input_line2[1]
        if command == 'Drive':
            distance, fuel = int(input_line2[2]), int(input_line2[3])
            result = drive(cars, car, distance, fuel)
            if isinstance(result, str):
                print(result)
            else:
                cars = result
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        elif command == 'Refuel':
            fuel = int(input_line2[2])
            cars, gas_refueled = refuel(cars, car, fuel)
            print(f"{car} refueled with {gas_refueled} liters")
        elif command == 'Revert':
            kilometers = int(input_line2[2])
            cars, flag = revert(cars, car, kilometers)
            if cars[car][0] >= 10000 and flag:
                print(f"{car} mileage decreased by {kilometers} kilometers")

        input_line2 = input()

    for key, value in cars.items():
        print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")

if __name__ == '__main__':
    main()