text = input()
total = 0

for i in range(0, len(text)):
    if text[i] == 'a':
        total += 1
    if text[i] == 'e':
        total += 2
    if text[i] == 'i':
        total += 3
    if text[i] == 'o':
        total += 4
    if text[i] == 'u':
        total += 5
print(total)
