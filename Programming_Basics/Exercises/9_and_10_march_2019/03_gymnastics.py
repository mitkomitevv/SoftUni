country = input()
category = input()
p1, p2 = 0, 0
total_points = 0

if country == 'Russia':
    if category == 'ribbon':
        p1 = 9.100
        p2 = 9.400
    elif category == 'hoop':
        p1 = 9.300
        p2 = 9.800
    elif category == 'rope':
        p1 = 9.600
        p2 = 9.000

if country == 'Bulgaria':
    if category == 'ribbon':
        p1 = 9.600
        p2 = 9.400
    elif category == 'hoop':
        p1 = 9.550
        p2 = 9.750
    elif category == 'rope':
        p1 = 9.500
        p2 = 9.400

if country == 'Italy':
    if category == 'ribbon':
        p1 = 9.200
        p2 = 9.500
    elif category == 'hoop':
        p1 = 9.450
        p2 = 9.350
    elif category == 'rope':
        p1 = 9.700
        p2 = 9.150

total_points = p1 + p2
percent = 100 - (total_points / 20) * 100

print(f'The team of {country} get {total_points:.3f} on {category}.')
print(f'{percent:.2f}%')
