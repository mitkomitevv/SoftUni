text = input()
letters = {}

for l in text:
    if l not in letters:
        letters[l] = text.count(l)

sorted_letters = {k: letters[k] for k in sorted(letters)}
for letter, count in sorted_letters.items():
    print(f"{letter}: {count} time/s")
