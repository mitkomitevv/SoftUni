import re

text = input()
pattern = r' ([a-z0-9]+[a-z0-9\.\-\_]*@[a-z\-]+\.[a-z\-]+[\.a-z]+)\b'
matches = re.findall(pattern, text)
print('\n'.join(matches))