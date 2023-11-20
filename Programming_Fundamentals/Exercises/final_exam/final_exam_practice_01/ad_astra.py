import re

text = input()
pattern = r"([#\|])([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.findall(pattern, text)

total_calories = sum(int(match[3]) for match in matches)

print(f"You have food to last you for: {total_calories // 2000} days!")

for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
