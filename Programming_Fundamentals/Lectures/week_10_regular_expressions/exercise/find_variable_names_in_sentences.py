import re

text = input()
pattern = r'\b\_([A-Za-z]+)\b'
matches = re.findall(pattern, text)
print(','.join(matches))
