import re

pattern = r"\d+"
while True:
    string = input()
    if string:
        matches = re.finditer(pattern, string)
        for match in matches:
            print(match[0], end=" ")
    else:
        break
