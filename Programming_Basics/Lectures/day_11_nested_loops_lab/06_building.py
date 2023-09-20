floors = int(input())
rooms = int(input())
for x in reversed(range(1, floors + 1)):
    for y in (range(rooms)):
        if x == floors:
            print(f'L{x}{y}', end=" ")
        elif x % 2 == 0:
            print(f'O{x}{y}', end=" ")
        else:
            print(f'A{x}{y}', end=" ")

    print()
