elements_sequence = input().split()
strings = input().split()
moves = 0
while strings[0] != 'end':
    if not elements_sequence:
        break
    moves += 1
    if int(strings[0]) < 0 or int(strings[1]) < 0 or int(strings[0]) >= len(elements_sequence) \
            or int(strings[1]) >= len(elements_sequence) or int(strings[0]) == int(strings[1]):
        middle = len(elements_sequence) // 2
        left, right = elements_sequence[:middle], elements_sequence[middle:]
        left.append(f"-{moves}a")
        left.append(f"-{moves}a")
        elements_sequence = left + right
        print('Invalid input! Adding additional elements to the board')
    elif elements_sequence[int(strings[0])] == elements_sequence[int(strings[1])]:
        print(f'Congrats! You have found matching elements - {elements_sequence[int(strings[0])]}!')
        elements_sequence = [x for i, x in enumerate(elements_sequence) if i not in [int(strings[0]), int(strings[1])]]
    else:
        print('Try again!')
    strings = input().split()
if not elements_sequence:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n"
          f"{' '.join(elements_sequence)}")
