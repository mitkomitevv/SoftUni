import re

line = input()
pattern = r"w{3}\.[A-Za-z0-9\-]+\.[a-z\.]+"
while line:
    match = re.search(pattern, line)
    if match:
        print(match.group())

    line = input()
