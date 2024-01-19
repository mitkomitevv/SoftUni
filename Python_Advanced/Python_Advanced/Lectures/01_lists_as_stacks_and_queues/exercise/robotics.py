from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
start_time = datetime.strptime(input(), "%H:%M:%S")
robots = {}

for robot in data:
    name, time = robot.split('-')
    robots[name] = [int(time), 0]

products = deque()
product = input()
while product != 'End':
    products.append(product)
    product = input()

while products:
    start_time += timedelta(seconds=1)

    for _, time in robots.items():
        if time[1] != 0:
            time[1] -= 1

    assigned = False
    for curr_robot, values in robots.items():
        if values[1] == 0:
            values[1] = values[0]
            curr_product = products.popleft()
            flag = True
            print(f"{curr_robot} - {curr_product} [{start_time.strftime('%H:%M:%S')}]")
            break

    if not assigned:
        products.rotate(-1)
