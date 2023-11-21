import re

num = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(num):
    string = input()
    match = re.search(pattern, string)
    if match:
        group = ''
        for char in match.group():
            if char.isdigit():
                group += char
        if group:
            print(f"Product group: {group}")
        else:
            print("Product group: 00")
    else:
        print(f"Invalid barcode")
