from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())
total_honey = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    curr_nectar = nectar.pop()

    if current_bee <= curr_nectar:
        if curr_nectar > 0:
            curr_symbol = symbols.popleft()
            if curr_symbol == '+':
                total_honey += abs(current_bee + curr_nectar)
            elif curr_symbol == '-':
                total_honey += abs(current_bee - curr_nectar)
            elif curr_symbol == '*':
                total_honey += abs(current_bee * curr_nectar)
            elif curr_symbol == '/':
                total_honey += abs(current_bee / curr_nectar)
    else:
        working_bees.appendleft(current_bee)


print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
