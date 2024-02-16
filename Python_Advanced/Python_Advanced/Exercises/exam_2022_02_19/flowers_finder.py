from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found = False

while vowels and consonants:
    char1, char2 = vowels.popleft(), consonants.pop()

    for word in words:
        words[word] = words[word].replace(char1, "")
        words[word] = words[word].replace(char2, "")
        if words[word] == "":
            found = True
            print(f"Word found: {word}")
            break
    if found:
        break

if not found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
