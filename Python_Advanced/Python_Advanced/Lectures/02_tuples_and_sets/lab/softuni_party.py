n = int(input())
guests = set()

for _ in range(n):
    code = input()
    guests.add(code)

code = input()
while code != 'END':
    if code in guests:
        guests.remove(code)

    code = input()

print(len(guests))
for guest in sorted(guests):
    print(guest)
