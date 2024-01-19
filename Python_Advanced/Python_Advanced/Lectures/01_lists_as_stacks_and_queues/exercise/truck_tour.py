from collections import deque

gas_pumps = int(input())
data = deque([int(x) for x in input().split()] for _ in range(gas_pumps))
data_copy = data.copy()
gas_in_tank = 0
pump_index = 0

while data_copy:
    gas, distance = data_copy.popleft()
    gas_in_tank += gas
    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        data.rotate(-1)
        data_copy = data.copy()
        pump_index += 1
        gas_in_tank = 0

print(pump_index)
