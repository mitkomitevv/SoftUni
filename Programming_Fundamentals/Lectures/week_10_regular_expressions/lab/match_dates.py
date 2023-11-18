import re

pattern = r'\b(\d{2})(-|\.|/)([A-Z][a-z]{2})\2(\d{4})\b'
matches = re.findall(pattern, input())

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# matches = re.finditer(regex, input())
# for match in matches:
#     print(f"Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}")
