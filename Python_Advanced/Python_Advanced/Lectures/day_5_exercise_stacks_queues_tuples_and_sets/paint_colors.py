from collections import deque

text = deque(input().split())

colors = {'red', 'yellow', 'blue', 'green', 'orange', 'purple'}
req_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

final_colors = []
while text:
    first = text.popleft()
    second = text.pop() if text else ''

    for color in(first + second, second + first):
        if color in colors:
            final_colors.append(color)
            break
    else:
        for string in(first[:-1], second[:-1]):
            if string:
                text.insert(len(text) // 2, string)

for color in set(req_colors).intersection(final_colors):
    if not req_colors[color].issubset(set(final_colors)):
        final_colors.remove(color)

print(final_colors)
