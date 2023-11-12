string = list(input())
explosion_strength = 0
final_string = ''
for idx in range(len(string)):
    if string[idx] != '>' and  explosion_strength > 0:
       explosion_strength -= 1
    elif string[idx] == '>':
        final_string += string[idx]
        explosion_strength += int(string[idx + 1])
    else:
        final_string += string[idx]

print(final_string)
