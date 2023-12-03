import re

num = int(input())
pattern = r'(\S+)>([\d]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1'

for _ in range(num):
    password = input()
    match = re.search(pattern, password)
    if match:
        print(f"Password: {match.group(2) + match.group(3) + match.group(4) + match.group(5)}")
    else:
        print("Try another password!")