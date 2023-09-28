n = int(input())
current_capacity = 255
capacity = current_capacity
filled = 0
for _ in range(n):
    litres = int(input())
    if current_capacity - litres < 0:
        print('Insufficient capacity!')
        continue
    else:
        filled += litres
    current_capacity -= litres
print(filled)
