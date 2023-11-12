some_string = input()
number = ''
current_string = ''
final_string = ''
for idx in range(len(some_string)):
    if not some_string[idx].isdigit():
        current_string += some_string[idx]
    else:
        number += some_string[idx]

    try:
        if some_string[idx + 1].isdigit():
            continue
    except IndexError:
        pass

    if number:
        final_string += int(number) * current_string.upper()
        current_string = ''
        number = ''

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
