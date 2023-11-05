input_line = input()
resources = {}
while input_line != 'stop':
    resource = input_line
    quantity = int(input())
    if resource not in resources.keys():
        resources[resource] = 0
    resources[resource] += quantity

    input_line = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
