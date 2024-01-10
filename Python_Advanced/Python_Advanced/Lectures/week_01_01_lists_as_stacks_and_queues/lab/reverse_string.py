from collections import deque

text = deque(input())

for _ in range(len(text)):
    print(text.pop(), end="")

# while text:
#     print(text.pop(), end="")
