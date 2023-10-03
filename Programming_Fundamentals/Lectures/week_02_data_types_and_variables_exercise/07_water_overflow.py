n = int(input())
capacity = 255
filled = 0
for _ in range(n):
    litres = int(input())
    if capacity - litres < 0:
        print('Insufficient capacity!')
        continue
    else:
        filled += litres
    capacity -= litres
print(filled)
