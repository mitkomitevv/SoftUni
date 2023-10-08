number = int(input())
counter = 0
for num in range(2, number):
    if number % num == 0:
        counter += 1
        break
if counter > 0:
    print('False')
else:
    print('True')
