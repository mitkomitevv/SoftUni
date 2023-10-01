string = input()
string_lower = string.lower()
words_for_count = ['sand', 'water', 'fish', 'sun']
counter = 0
for word in words_for_count:
    counter += string_lower.count(word)
print(counter)
