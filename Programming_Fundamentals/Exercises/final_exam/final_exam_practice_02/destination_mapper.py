import re

text = input()
pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, text)
print(f'Destinations: {", ".join([match[1] for match in matches])}')
print(f"Travel Points: {sum(len(match[1]) for match in matches)}")
