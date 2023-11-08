input_line = input()
info = {}

while input_line != 'End':
    company, ID = input_line.split(' -> ')
    if company not in info:
        info[company] = []
    if ID not in info[company]:
        info[company].append(ID)
    input_line = input()

for key, value in info.items():
    print(key)
    for ID in value:
        print(f'-- {ID}')