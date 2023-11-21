import re

text = input()
mirror_words = []
pattern = r'([#@])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
matches = re.findall(pattern, text)

for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(f"{match[1]} <=> {match[2]}")

if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print('No word pairs found!')

if mirror_words:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print("No mirror words!")
