from collections import deque

parentheses = deque(input())
open_parens = deque()

while parentheses:
    current_paren = parentheses.popleft()

    if current_paren in "([{":
        open_parens.append(current_paren)
    elif not open_parens:
        print("NO")
        break
    else:
        if open_parens.pop() + current_paren not in "()[]{}":
            print("NO")
            break
else:
    print("YES")
