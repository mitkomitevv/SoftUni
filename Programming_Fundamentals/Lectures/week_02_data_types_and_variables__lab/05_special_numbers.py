number = int(input())
for current_number in range(1, number + 1):
    special_or_not = 0
    number_as_string = str(current_number)
    for digit in number_as_string:
        special_or_not += int(digit)
    special = False
    if special_or_not == 5 or special_or_not == 7 or special_or_not == 11:
        special = True
    print(f'{current_number} -> {special}')
