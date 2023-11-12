n = int(input())
name = ''
age = ''
for _ in range(n):
    text = input().split()

    for word in text:
        if '@' in word and '|' in word:
            idx1, idx2 = word.index('@'), word.index('|')
            name = word[idx1 + 1:idx2]
        if '#' in word and '*' in word:
            idx1, idx2 = word.index('#'), word.index('*')
            age = int(word[idx1 + 1:idx2])

    print(f"{name} is {age} years old.")
