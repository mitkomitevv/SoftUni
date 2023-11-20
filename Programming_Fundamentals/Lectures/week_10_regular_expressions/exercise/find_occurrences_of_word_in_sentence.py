import re

text = input()
word_to_find = input()
pattern = fr'\b{word_to_find}\b'
matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))
