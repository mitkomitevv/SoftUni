from collections import deque

green_window = int(input())
free_window = int(input())

car_passed = 0
cars = deque()
crash = False

while True:
    data = input()

    if data == "END":
        break

    if data != "green":
        cars.append(data)
    else:
        current_green_window = green_window

        while current_green_window > 0 and cars:
            car = cars.popleft()
            time_to_pass = len(car)

            if time_to_pass <= current_green_window:
                current_green_window -= time_to_pass
                car_passed += 1
            elif time_to_pass <= current_green_window + free_window:
                car_passed += 1
                break
            else:
                print(f"A crash happened!\n"
                      f"{car} was hit at {car[current_green_window + free_window]}.")
                crash = True
                break

    if crash:
        break

if not crash:
    print("Everyone is safe.")
    print(f"{car_passed} total cars passed the crossroads.")
