number = int(input())
counter = 0
for num in range(2, number + 1):
    if number % num == 0:
        counter += 1
if counter > 1:
    print('False')
else:
    print('True')
