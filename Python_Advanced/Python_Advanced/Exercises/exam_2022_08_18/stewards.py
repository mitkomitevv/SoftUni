from collections import deque

seats = input().split(', ')
seq1 = deque(int(x) for x in input().split(', '))
seq2 = deque(int(x) for x in input().split(', '))


taken_seats = []
rotations = 0

while rotations < 10 and len(taken_seats) < 3:
    num1, num2= seq1.popleft(), seq2.pop()
    result1, result2 = str(num1) + chr(num1 + num2), str(num2) + chr(num1 + num2)

    if result1 in seats or result2 in seats:
        taken_seats.append(seats.pop(seats.index(result1)) if result1 in seats else seats.pop(seats.index(result2)))
    else:
        seq1.append(num1)
        seq2.appendleft(num2)

    rotations += 1

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
