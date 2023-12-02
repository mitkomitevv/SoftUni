import re

text = input()
cool_threshold = 1

for char in text:
    if char.isdigit():
       cool_threshold *= int(char)

print(f"Cool threshold: {cool_threshold}")

pattern = r'(\*\*|::)([A-Z][a-z]{2,})\1'
matches = re.findall(pattern, text)

print(f"{len(matches)} emojis found in the text. The cool ones are:")
for emoji in matches:
    surrounding_character = emoji[0]
    word = emoji[1]
    cool_or_not = sum(list(ord(x) for x in word))
    if cool_or_not > cool_threshold:
        print(surrounding_character + word + surrounding_character)
